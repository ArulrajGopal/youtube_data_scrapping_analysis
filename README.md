# youtube data scrapping and analytics

## Project objective
Fetch real youtube data of few channels and load it into structured database and get some insights


## steps to setup

1. Install python and pip install as below.

            python --version

            pip install -r requirements.txt

2. Install postgreSQL in local or setup postgreSQL server at cloud. In case of local install, use below to check the version. 
Get server name, database name, user name and password. In case of local install, server name will be localhost

            psql --version

3. Setup AWS environment and get access_key_id & secret_access_key


4. Get into youtube developer console and get youtube_api_key and set up in below variable.
google developer console --> create new project --> Enable "youtube data API 3" api --> create API key at credentials


5. Set below environment variables. 

        nano ~/.bashrc

        export youtube_api_key="your_youtube_api_key"
        export aws_access_key_id="your_aws_access_key_id"
        export aws_secret_access_key="your_aws_secret_access_key"
        export postgress_user="your_postgres_user"
        export postgres_password="your_postgres_password"
        export postgres_server="your_postgres_server"
        export postgres_port="5432"
        export database_name="your_database_name"

        source ~/.bashrc

6. Run main.py




Finally, the youtube dashboard is ready at the website!!!




