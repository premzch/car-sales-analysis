import pandas as pd
import numpy as np

df = pd.read_csv("Car Sales.csv", encoding='latin1')
print("--- Initial Data Check ---")
print(df.info())
print("\n--- Missing Values Per Column ---")
print(df.isnull().sum())
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
df = df.rename(columns={
    'car_id': 'car_id',
    'dealer_no': 'dealer_zip_code' 
})

if 'engine' in df.columns:
    df['engine'] = df['engine'].str.replace('Â', '', regex=False).str.strip()

text_cols = ['customer_name', 'gender', 'dealer_name', 'company', 'model', 'engine', 'transmission', 'color', 'body_style', 'dealer_region']
for col in text_cols:
    if col in df.columns:
        df[col] = df[col].str.strip().str.title()
df['date'] = pd.to_datetime(df['date'], errors='coerce')
df['annual_income'] = pd.to_numeric(df['annual_income'], errors='coerce')
df['price_($)'] = pd.to_numeric(df['price_($)'], errors='coerce')
df = df.rename(columns={'price_($)': 'price'})
print("\n--- Cleaned Data Check ---")
print(df.info())
print(df.head())
df.to_csv("Car_Sales_Cleaned.csv",)
