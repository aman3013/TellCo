# scripts/data_loading.py

import os
import psycopg2
import sys
import numpy as np
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine

sys.path.append(os.path.abspath(os.path.join("./scripts/")))
# Load environment variables from .env file
load_dotenv()

# Fetch database connection parameters from environment variables
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
def load_data_using_sqlalchemy(query):
    """
    Connects to the PostgreSQL database and loads data based on the provided SQL query using SQLAlchemy.

    :param query: SQL query to execute.
    :return: DataFrame containing the results of the query.
    """
    try:
        # Create a connection string
        connection_string = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

        # Create an SQLAlchemy engine
        engine = create_engine(connection_string)

        # Load data into a pandas DataFrame
        df = pd.read_sql_query(query, engine)

        return df

    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    

from typing import Optional



class CleanTelco:
    
    def convert_to_datetime(self, df: pd.DataFrame, col_name) -> pd.DataFrame:
        try:
            df[col_name] = pd.to_datetime(df[col_name], errors='coerce')
            print('Converted to datetime')
        except Exception as e:
            print(f"Error converting to datetime: {e}")
        return df
    
    def convert_to_integer(self, df: pd.DataFrame, col_name)-> pd.DataFrame:
        try:
            df[col_name] = df[col_name].astype("int64")
            print('Converted to integer')
        except Exception as e:
            print(f"Error converting to integer: {e}")
        return df
    
    def convert_to_string(self,  df: pd.DataFrame, col_name) -> pd.DataFrame:
        try:
            df[col_name] = df[col_name].astype("string")
            print('Converted to string')
        except Exception as e:
            print(f"Error converting to string: {e}")
        return df

    def drop_duplicate(self, df: pd.DataFrame) -> pd.DataFrame:
        try:
            df = df.drop_duplicates()
            print('Dropped duplicates')
        except Exception as e:
            print(f"Error dropping duplicates: {e}")
        return df

    def drop_column(self, df: pd.DataFrame, col_name) -> pd.DataFrame:
        try:
            df.drop([col_name], axis=1, inplace=True)
            print('Dropped column')
        except Exception as e:
            print(f"Error dropping column: {e}")
        return df

    def get_percentage_missing (self, df: pd.DataFrame) -> pd.DataFrame:   
        try:
            missing_percentage = df.isnull().sum() * 100 / len(df)
            missing_value_df = pd.DataFrame({'column_name': df.columns,
                                            'percent_missing': missing_percentage})
            missing_value_df.sort_values('percent_missing', inplace=True)
            print('Got percentage of missing values')
        except Exception as e:
            print(f"Error getting percentage of missing values: {e}")
            missing_value_df = pd.DataFrame()
        return missing_value_df

    def get_missing_values(self, df: pd.DataFrame) -> pd.DataFrame:
        try:
            percent_missing = df.isnull().sum() * 100 / len(df)
            missing_value_df = pd.DataFrame({'column_name': df.columns,
                                            'percent_missing': percent_missing})
            missing_value_df.sort_values('percent_missing', inplace=True)
            print('Got missing values')
        except Exception as e:
            print(f"Error getting missing values: {e}")
            missing_value_df = pd.DataFrame()
        return missing_value_df
        
    def fix_missing_ffill(self,  df: pd.DataFrame, col_name) -> pd.DataFrame:
        try:
            df[col_name] = df[col_name].fillna(method='ffill')
            print('Fixed missing values with forward fill')
        except Exception as e:
            print(f"Error fixing missing values with forward fill: {e}")
        return df

    def fix_missing_bfill(self,  df: pd.DataFrame, col_name) -> pd.DataFrame:
        try:
            df[col_name] = df[col_name].fillna(method='bfill')
            print('Fixed missing values with backward fill')
        except Exception as e:
            print(f"Error fixing missing values with backward fill: {e}")
        return df

    def fix_missing_value(self,  df: pd.DataFrame, col_name, value) -> pd.DataFrame:
        try:
            df[col_name] = df[col_name].fillna(value)
            print(f'Fixed missing values with {value}')
        except Exception as e:
            print(f"Error fixing missing values with specific value: {e}")
        return df

    def fix_missing_median(self,  df: pd.DataFrame, col_name) -> pd.DataFrame:
        try:
            df[col_name] = df[col_name].fillna(df[col_name].median())
            print('Fixed missing values with median')
        except Exception as e:
            print(f"Error fixing missing values with median: {e}")
        return df

    def get_row_nan_percentage(self,  df: pd.DataFrame) -> Optional[float]:
        try:
            rows_with_nan = [index for index, row in df.iterrows() if row.isnull().any()]
            percentage = (len(rows_with_nan) / df.shape[0]) * 100
            print(f'Percentage of rows with NaN: {percentage}%')
            return percentage
        except Exception as e:
            print(f"Error calculating row NaN percentage: {e}")
            return None

    def fix_outliers(self, df: pd.DataFrame) -> pd.DataFrame:
        try:
            for col in df.select_dtypes('float64').columns.tolist():
                Q1 = df[col].quantile(0.25)
                Q3 = df[col].quantile(0.75)
                IQR = Q3 - Q1
                lower = Q1 - (IQR * 1.5)
                upper = Q3 + (IQR * 1.5)

                df[col] = np.where(df[col] > upper, upper, df[col])
                df[col] = np.where(df[col] < lower, lower, df[col])
            print('Fixed outliers')
        except Exception as e:
            print(f"Error fixing outliers: {e}")
        return df

