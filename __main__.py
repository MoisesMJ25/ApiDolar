import os
import logging
from modules import DataConn, ApiData
from dotenv import load_dotenv

APIS = {
    'blue' : 'https://dolarapi.com/v1/dolares/blue',
    'ccl' : 'https://dolarapi.com/v1/dolares/contadoconliqui',
    'cripto' : 'https://dolarapi.com/v1/dolares/cripto',
    'mayorista' : 'https://dolarapi.com/v1/dolares/mayorista',
    'oficial' : 'https://dolarapi.com/v1/dolares/oficial',
    'bolsa': 'https://dolarapi.com/v1/dolares/bolsa',
    'tarjeta': 'https://dolarapi.com/v1/dolares/tarjeta'
    }

logging.basicConfig(
    filename='app.log',
    filemode='a',
    format='%(asctime)s ::MainModule-> %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)

load_dotenv()

def main():
    user_credentials = {
        "REDSHIFT_USERNAME" : os.getenv('REDSHIFT_USERNAME'),
        "REDSHIFT_PASSWORD" : os.getenv('REDSHIFT_PASSWORD'),
        "REDSHIFT_HOST" : os.getenv('REDSHIFT_HOST'),
        "REDSHIFT_PORT" : os.getenv('REDSHIFT_PORT', '5439'),
        "REDSHIFT_DBNAME" : os.getenv('REDSHIFT_DBNAME')
    }

    schema:str = "moisesmarquinaj_coderhouse"
    table:str = "api_dolar"

    data_conn = DataConn(user_credentials, schema)


    try:
        data = ApiData.get_api(APIS)
        data_conn.upload_data(data, 'api_dolar')
        logging.info(f"Data uploaded to -> {schema}.{table}")

    except Exception as e:
        logging.error(f"Not able to upload data\n{e}")

    finally:
        data_conn.close_conn()

if __name__ == "__main__":
    main()
    