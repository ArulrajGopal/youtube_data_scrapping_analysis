import os
import boto3
import psycopg2

youtube_api_key = os.environ.get("youtube_api_key")
aws_access_key_id=os.environ.get("aws_access_key_id")
aws_secret_access_key= os.environ.get("aws_secret_access_key")
postgress_user = os.environ.get("postgress_user")
postgres_password = os.environ.get("postgres_password")

logging_path = ""

channel_id_dict= {
"EQSIS":"UCKTWY-rVwUqCxrVmPOlJyjA"
,"OPTIONWITHAK":"UCslsTpdkrVnZSwxawhJN6Ag"
,"financeboosan":"UCmfl6VteCu880D8Txl4vEag"
,"CapitalZone":"UCxoM_zP4Cr9LpIEn3TEZhvg"
,"TheMadrasTrader":"UCqxH7wzv-sMrCnjP3lM3Nmw"
,"SagaContraTrading":"UChaRiZ3h9JlLCeO2pdWkxMw"
,"ddnifty":"UCYRB8kDbaW6a1Gufr_qwVTA"
,"TamilStockMarket":"UC8HLa3_4B_31-UMSiLXrsCQ"
,"HumbledVillageTrader":"UCoxNE6QEFUAdKuqvjT-kNwA"
,"TamilShare":"UCaGwH4JooqsvBt-gJtB85Lg"
# ,"TiruppurBullsShares":"UCqhL6vNCwYLC9_jePXOIvBg"
# ,"PRSundar":"UCS2NdYUmv_PUyyKeDAo5zYA"
# ,"Muthaleetukalam":"UCahsYnjbRheSL7uv6jWbJ4w"
# ,"CauveryBusiness" : "UCa1FSXPOxb0x8lZTYCbQJ5g"
# ,"MoneyPechu" : "UC7fQFl37yAOaPaoxQm-TqSA"
# ,"TradeAchievers":"UCzk4zJEoZMnjvpoN0HlKjHQ"
}


dynamodb = boto3.resource(
    'dynamodb',
    region_name='us-east-1', 
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key
)

postgresql = psycopg2.connect(
            host="localhost",
            dbname="my_database",
            user=postgress_user,
            password = postgres_password,
            port="5432"
)