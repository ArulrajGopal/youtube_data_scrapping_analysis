import os
import boto3
from googleapiclient.discovery import build
from config import *

# environment variables
youtube_api_key = os.environ.get("youtube_api_key")
aws_access_key_id=os.environ.get("aws_access_key_id")
aws_secret_access_key= os.environ.get("aws_secret_access_key")
postgress_user = os.environ.get("postgress_user")
postgres_password = os.environ.get("postgres_password")


# configurations
youtube =  build("youtube","v3",developerKey=youtube_api_key)

dynamodb_resource = boto3.resource(
    'dynamodb',
    region_name='us-east-1', 
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key
)

dynamodb_client = boto3.client(
    'dynamodb',
    region_name='us-east-1',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key
)

# PostgreSQL connection details
db_user = postgress_user
db_password = postgres_password
db_host = 'localhost'       
db_port = '5432'
db_name = 'postgres'

# In channel_id_config, the third element indicates whether to process the channel or not
# True means process, False means skip
# second element is channel_id, first element is channel_name
channel_id_config= [
    ["Akshat Shrivastava", "UCqW8jxh4tH1Z1sWPbkGWL4g", True],
    ["CA Rachana Phadke Ranade", "UCe3qdG0A_gr-sEdat5y2twQ", True],
    ["MoneyPechu", "UC7fQFl37yAOaPaoxQm-TqSA", True],
    ["Finance With Sharan", "UCwVEhEzsjLym_u1he4XWFkg", True],
    ["PRSundar", "UCS2NdYUmv_PUyyKeDAo5zYA", False],
    ["Be Rich", "UCZ-RwglseBp2cAuHwYGb91Q", False],
    ["EQSIS", "UCKTWY-rVwUqCxrVmPOlJyjA", False],
    ["financeboosan", "UCmfl6VteCu880D8Txl4vEag", False],
    ["CapitalZone", "UCxoM_zP4Cr9LpIEn3TEZhvg", False],
    ["TheMadrasTrader", "UCqxH7wzv-sMrCnjP3lM3Nmw", False],
    ["SagaContraTrading", "UChaRiZ3h9JlLCeO2pdWkxMw", False],
    ["ddnifty", "UCYRB8kDbaW6a1Gufr_qwVTA", False],
    ["TamilStockMarket", "UC8HLa3_4B_31-UMSiLXrsCQ", False],
    ["HumbledVillageTrader", "UCoxNE6QEFUAdKuqvjT-kNwA", False],
    ["TamilShare", "UCaGwH4JooqsvBt-gJtB85Lg", False],
    ["TiruppurBullsShares", "UCqhL6vNCwYLC9_jePXOIvBg", False],
    ["Muthaleetukalam", "UCahsYnjbRheSL7uv6jWbJ4w", False],
    ["CauveryBusiness", "UCa1FSXPOxb0x8lZTYCbQJ5g", False],
    ["TradeAchievers", "UCzk4zJEoZMnjvpoN0HlKjHQ", False]
]














