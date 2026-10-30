import pandas as pd
import ssl

csv_file = 'https://drive.google.com/uc?id=1ujY0WCcePdotG2xdbLyeECFW9lCJ4t-K&export=download'
#Temporary fix
ssl._create_default_https_context = ssl._create_unverified_context


try:
    df = pd.read_csv(csv_file,engine='pyarrow',on_bad_lines='skip')
    outfile = 'sales_data_test.csv'
    df.head(10).to_csv(outfile, index=False)
    print(f"First 10 rows of {csv_file} saved to {outfile}")

except Exception as e:
    print("Error reading the CSV file:", e)

#Temporary fix
ssl._create_default_https_context = ssl._create_unverified_context


try:
    df = pd.read_csv(csv_file,engine='pyarrow',on_bad_lines='skip')
    print(df.head())
except Exception as e:
    print("Error reading the CSV file:", e)
