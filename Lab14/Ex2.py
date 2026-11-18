# Grab 1 month interest rate from the US Treasury website.
import ssl, lxml
import pandas as pd
import urllib.request

url = "https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value_month=202603"
print("Retrieving", url)

webpage = urllib.request.urlopen(url)
df = pd.read_html(webpage)
print("Columns:", df[0].columns)

int_rate_table = df[0]

# Print the table of 1 month interest rates
print("1 Month Interest Rates:")

for index, row in int_rate_table.iterrows():
    print(f"Date: {row['Date']}, 1 Month Rate: {row['1 Mo']}")
