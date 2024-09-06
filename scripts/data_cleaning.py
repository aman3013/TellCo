import os
import pandas as pd

def convert_bytes_to_megabytes(df, column_name):
    # Convert bytes to megabytes (1 MB = 1,048,576 bytes)
    df[column_name] = df[column_name] / (1024 * 1024)
    return df[column_name]

def missing_values_table(df):
    # Total missing values
    missing_values = df.isnull().sum()
    
    # Percentage of missing values
    missing_percentage = 100 * df.isnull().sum() / len(df)
    
    # Create a DataFrame with the results
    missing_values_df = pd.DataFrame({'Missing Values': missing_values, 'Percentage': missing_percentage})
    
    # Filter out columns with no missing values
    missing_values_df = missing_values_df[missing_values_df['Missing Values'] > 0]
    
    # Sort the DataFrame by percentage of missing values in descending order
    missing_values_df = missing_values_df.sort_values(by='Percentage', ascending=False)
    
    return missing_values_df
import numpy as np

# Custom function to fix outliers using the IQR method
def fix_outliers(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    # Replace outliers with NaN or cap them
    df[column] = np.where(df[column] < lower_bound, lower_bound, df[column])
    df[column] = np.where(df[column] > upper_bound, upper_bound, df[column])
    
    return df


