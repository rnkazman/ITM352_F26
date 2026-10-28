# Import homes data and create a dataframe
import pandas as pd

homes_data_file = 'https://drive.google.com/uc?id=1M-X_bypJJ6K5p6eM6aYBwt1qIizIiIex&export=download'
homes_df = pd.read_csv(homes_data_file)
print(homes_df.head())

# Print the dimensions of the dataframe
shape = homes_df.shape
print("The dimensions of the dataframe are:", shape)

# Only keep properties with more than 500 units and drop the easement column

df_big = homes_df[homes_df['units'] >= 500]
df_big= df_big.drop(columns=['easement'])
print(df_big.head(10))

# Look at the data types
print(df_big.info())

# Coerce land_sqft, gross_sqft, and sale_price to numeric
df_big['land_sqft'] = pd.to_numeric(df_big['land_sqft'], errors='coerce')
df_big['gross_sqft'] = pd.to_numeric(df_big['gross_sqft'], errors='coerce')
df_big['sale_price'] = pd.to_numeric(df_big['sale_price'], errors='coerce')

# We have some null values. Drop these.
df_big = df_big.dropna()

# Now drop duplicate records.
df_big = df_big.drop_duplicates()

# Filter out 0 sales
df_big = df_big[df_big['sale_price'] > 0]
print("After filtering out 0 sales...")
print(df_big.info())
print(df_big.head(10))
