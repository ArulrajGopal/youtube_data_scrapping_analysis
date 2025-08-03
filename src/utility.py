from config import *


def load_dyanmo_db(table_name,value):
    table = dynamodb.Table(table_name)
    table.put_item(Item=value)

def read_dyanmo_db(table_name):
    table = dynamodb.Table(table_name)
    response = table.scan()
    data = response['Items']
    return data





