import os
import sys
from src.mlproject.exception import CustomException
from src.mlproject.logger import logging
import pandas as pd
from dotenv import load_dotenv
import pymysql


load_dotenv()

host = os.getenve("host")
user = os.getenve("user")
password = os.getenv("password")
df = os.getenv("db")



def read_sql_data():
    logging.info("Reading SQL database started")
    try:
        mydb = pymysql.connect
    except Exception as ex:
        raise CustomException()
    
