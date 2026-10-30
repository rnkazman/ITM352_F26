# Create a dataframe from a CSV file and create a pivot table aggregating sales by region and order_type.
# Name: Rick Kazman
# Date: Oct. 30, 2026

import pandas as pd
import numpy as np
import ssl

# Ignore SSL certificate errors
ssl._create_default_https_context = ssl._create_unverified_context
# Tell Pandas to print all columns when displaying a DataFrame
pd.set_option('display.max_columns', None)

csv_file = 'https://drive.google.com/uc?id=1ujY0WCcePdotG2xdbLyeECFW9lCJ4t-K&export=download'

try:
    df = pd.read_csv(csv_file, engine='pyarrow', on_bad_lines='skip')
    df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')
    # print(df.head())

    # Calculate sales total per row, for later use in the pivot table.
    df['sales'] = df['quantity'] * df['unit_price']

    # Create a pivot table aggregating sales by region and order_type
    pivot_table = pd.pivot_table(df,
                                 values='sales',
                                 index='sales_region',
                                 columns='order_type',
                                 aggfunc=np.sum,
                                 margins=True,
                                 margins_name='Total Sales')

    print(pivot_table)

except Exception as e:
    print(f"Error occurred while reading the CSV file: {e}")