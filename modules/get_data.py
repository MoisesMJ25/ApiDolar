import requests
import pandas as pd
import logging

logging.basicConfig(
    filename='app.log',
    filemode='a',
    format='%(asctime)s ::GetDataModule-> %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)


class ApiData:
    def __init__(self):
        dict

    def get_api(self):

        try:
            data = [requests.get(i).json() for i in self.values()]
            data = pd.DataFrame(data)
            data = data.drop('nombre', axis=1)
            data = data.reindex(['casa','moneda','compra','venta', 'fechaActualizacion'], axis=1)
            data = data.rename(columns={'fechaActualizacion':'fecha'})
            print(data)
            return data

        except Exception as e:
            logging.error(f"Data not found\n{e}")
            raise
