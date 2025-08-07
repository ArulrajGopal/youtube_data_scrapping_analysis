import os
import boto3
from googleapiclient.discovery import build

youtube_api_key = os.environ.get("youtube_api_key")
youtube =  build("youtube","v3",developerKey=youtube_api_key)

aws_access_key_id=os.environ.get("aws_access_key_id")
aws_secret_access_key= os.environ.get("aws_secret_access_key")

postgress_user = os.environ.get("postgress_user")
postgres_password = os.environ.get("postgres_password")


# PostgreSQL connection details
db_user = postgress_user
db_password = postgres_password
db_host = 'localhost'       
db_port = '5432'
db_name = 'postgres'

channel_id_dict= {
"OPTIONWITHAK":"UCslsTpdkrVnZSwxawhJN6Ag"
,"EQSIS":"UCKTWY-rVwUqCxrVmPOlJyjA"
,"financeboosan":"UCmfl6VteCu880D8Txl4vEag"
,"CapitalZone":"UCxoM_zP4Cr9LpIEn3TEZhvg"
,"TheMadrasTrader":"UCqxH7wzv-sMrCnjP3lM3Nmw"
,"SagaContraTrading":"UChaRiZ3h9JlLCeO2pdWkxMw"
,"ddnifty":"UCYRB8kDbaW6a1Gufr_qwVTA"
,"TamilStockMarket":"UC8HLa3_4B_31-UMSiLXrsCQ"
,"HumbledVillageTrader":"UCoxNE6QEFUAdKuqvjT-kNwA"
,"TamilShare":"UCaGwH4JooqsvBt-gJtB85Lg"
,"TiruppurBullsShares":"UCqhL6vNCwYLC9_jePXOIvBg"
,"PRSundar":"UCS2NdYUmv_PUyyKeDAo5zYA"
,"Muthaleetukalam":"UCahsYnjbRheSL7uv6jWbJ4w"
,"CauveryBusiness" : "UCa1FSXPOxb0x8lZTYCbQJ5g"
,"MoneyPechu" : "UC7fQFl37yAOaPaoxQm-TqSA"
,"TradeAchievers":"UCzk4zJEoZMnjvpoN0HlKjHQ"
}

# Akshat Shrivastava, CA Rachana Phadke Ranade, finance with sharan, be rich, pr sundar

dynamodb = boto3.resource(
    'dynamodb',
    region_name='us-east-1', 
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key
)








