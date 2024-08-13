from datetime import date
import pandas as pd

df = pd.read_csv(r"raw_dataset\Sales.csv")

# conversion of object datatype to datetime
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Delivery Date'] = pd.to_datetime(df['Delivery Date'])

# Calculate the delivery duration
df['delivery_duration'] = (df['Delivery Date'] - df['Order Date']).dt.days

# Compute the average delivery duration
average_duration = df['delivery_duration'].mean()
average_duration

# newly imputed delivery date for Nan data
df['Delivery Date'] = df.apply(
    lambda row: row['Order Date'] + pd.Timedelta(days=average_duration) if pd.isnull(row['Delivery Date']) else row[
        'Delivery Date'], axis=1)
df['Delivery Date'] = df['Delivery Date'].dt.date

df.drop(['delivery_duration'], axis=1, inplace=True)
df['Delivery Date'] = pd.to_datetime(df['Delivery Date'])
# df = df.rename(columns={'Order Date': 'Date'})

df.to_csv("cleaned_dataset\cleaned_sales_dataset.csv", index=False)

df = pd.read_csv(r"raw_dataset\Products.csv")

# converting object to float

df['Unit Cost USD'] = df['Unit Cost USD'].str.replace('$', '')
df['Unit Cost USD'] = df['Unit Cost USD'].str.replace(',', '')
df['Unit Cost USD'] = df['Unit Cost USD'].astype(float)

df['Unit Price USD'] = df['Unit Price USD'].str.replace('$', '')
df['Unit Price USD'] = df['Unit Price USD'].str.replace(',', '')
df['Unit Price USD'] = df['Unit Price USD'].astype(float)

df.to_csv("cleaned_dataset\cleaned_product_dataset.csv", index=False)

df = pd.read_csv(r"raw_dataset\Stores.csv")

df['Open Date'] = pd.to_datetime(df['Open Date'])
df = df.dropna()

df.to_csv("cleaned_dataset\cleaned_stores_dataset.csv", index=False)

df = pd.read_csv(r"raw_dataset\Exchange_Rates.csv")

df['Date'] = pd.to_datetime(df['Date'])
df = df.rename(columns={'Currency': 'Currency Code'})

df.to_csv("cleaned_dataset\cleaned_exchangerate_dataset.csv", index=False)

df = pd.read_csv(r"raw_dataset\Customers.csv", encoding='latin1')

df['Birthday'] = pd.to_datetime(df['Birthday'])

age_data = []

# converting Birthday to Age
for val in df['Birthday']:
    age = (date.today()).year - val.year
    age_data.append(age)
df['Age'] = age_data

df.to_csv("cleaned_dataset\cleaned_customer_dataset.csv", index=False)
