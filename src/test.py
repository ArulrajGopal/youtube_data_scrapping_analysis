from datetime import datetime
from config import *
from utility import *
from googleapiclient.errors import HttpError
import uuid
import botocore.exceptions


def table_exists(table_name):
    try:
        response = dynamodb_client.describe_table(TableName=table_name)
        return response["Table"]["TableStatus"]
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == 'ResourceNotFoundException':
            return None
        else:
            raise

def create_table_if_not_exists(table_name, primary_key):
    status = table_exists(table_name)

    if status == "ACTIVE":
        print(f"Table '{table_name}' already exists and is ACTIVE.")
        return
    elif status == "CREATING":
        print(f"Table '{table_name}' is still being created. Waiting...")
        waiter = dynamodb_client.get_waiter('table_exists')
        waiter.wait(TableName=table_name)
        return
    elif status == "DELETING":
        print(f"Table '{table_name}' is being deleted. Waiting...")
        waiter = dynamodb_client.get_waiter('table_not_exists')
        waiter.wait(TableName=table_name)

    # Safe to create
    response = dynamodb_client.create_table(
        TableName=table_name,
        KeySchema=[{'AttributeName': primary_key, 'KeyType': 'HASH'}],
        AttributeDefinitions=[{'AttributeName': primary_key, 'AttributeType': 'S'}],
        BillingMode='PAY_PER_REQUEST'
    )
    print(f"Creating table '{table_name}'...")
    waiter = dynamodb_client.get_waiter('table_exists')
    waiter.wait(TableName=table_name)
    print(f"Table '{table_name}' is ready.")


def delete_table(table_name):
    try:
        print(f"Deleting table '{table_name}'...")
        dynamodb_client.delete_table(TableName=table_name)

        waiter = dynamodb_client.get_waiter('table_not_exists')
        waiter.wait(TableName=table_name)
        print(f"Table '{table_name}' deleted successfully.")
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == 'ResourceNotFoundException':
            print(f"Table '{table_name}' does not exist.")
        else:
            raise


def load_dyanmo_db(table_name, value, primary_key, is_replace=False):
    if is_replace:
        delete_table(table_name)

    # Always safe-create table
    create_table_if_not_exists(table_name, primary_key)

    # Insert record
    table = dynamodb_resource.Table(table_name)
    table.put_item(Item=value)
    print(f"Inserted item into '{table_name}': {value}")


def get_popular_comments(video_id_list):
  current_date = int(datetime.now().strftime("%Y%m%d%H"))
  all_popular_comments = []

  for video_id in video_id_list:
    try:
      request = youtube.commentThreads().list(part="snippet", maxResults=100,order="relevance",videoId=video_id)
      response = request.execute()

      comments_list = response["items"]

      for comment in comments_list:
        current_time = str(datetime.now())
        comment['comment_id'] = str(uuid.uuid4())
        comment["load_dt"] = current_date
        comment["updated_time"] = current_time
        all_popular_comments.append(comment)

    except HttpError as e:
        print(f"Failed to fetch comments for video ID {video_id}: {e}")

  return all_popular_comments




video_id_list = ["P_gV1uvwYbI","CuRzpot5c5g","6MtiylZC_eM","pIX_zytsvLI","ECpin233eTU"]
video_id_list = ["P_gV1uvwYbI"]

popular_comments_lst = get_popular_comments(video_id_list)
print("popular comments extracted successfully!")


for response in popular_comments_lst:
    load_dyanmo_db("comment_details_raw",response,"comment_id", is_replace=True)
print("comment details loaded into dynamoDB successfully!")



