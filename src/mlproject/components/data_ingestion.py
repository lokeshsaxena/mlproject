import os
import sys
from src.mlproject.exception import CustomException
from src.mlproject.logger import logging
import pandas as pd


from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_data_path:str = os.path.join('artifacts', 'train.csv')
    test_data_path:str = os.path.join('artifacts', 'test.csv')
    raw_data_path:str = os.path.join('artifacts', 'raw .csv')

class DataIngestion:
    def __init__(self):
        self.ingenstion_confing = DataIngestionConfig()

    def initiate_data_ingestion(self):
        try:
            ##reading the data from SQL
            logging.info("Reading from SQL database")

            os.makedirs(os.path.dirname(self.ingenstion_confing.train_data_path), exist_ok=True)
            
            df.

        except Exception as e:
            raise CustomException(e, sys)
        

        
