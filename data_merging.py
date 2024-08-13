import pandas as pd

sales_data = pd.read_csv(r"cleaned_dataset\cleaned_sales_dataset.csv", parse_dates=['Order Date', 'Delivery Date'])
product_data = pd.read_csv(r"cleaned_dataset\cleaned_product_dataset.csv")
stores_data = pd.read_csv(r"cleaned_dataset\cleaned_stores_dataset.csv", parse_dates=['Open Date'])
exchange_data = pd.read_csv(r"cleaned_dataset\cleaned_exchangerate_dataset.csv", parse_dates=['Date'])
customer_data = pd.read_csv(r"cleaned_dataset\cleaned_customer_dataset.csv", encoding='latin1',
                            parse_dates=['Birthday'])
merged_data = pd.merge(sales_data, product_data, on='ProductKey')

merged_data.to_csv("merged_dataset\sales_product_data.csv", index=False)

merged_data1 = pd.merge(sales_data, customer_data, on='CustomerKey')
merged_data1.to_csv("merged_dataset\sales_customer_data.csv", index=False)

merged_data2 = pd.merge(sales_data, stores_data, on='StoreKey')
merged_data2.to_csv("merged_dataset\sales_store_data.csv", index=False)

sales_data = pd.read_csv(r"cleaned_dataset\cleaned_sales_dataset.csv")
exchange_data = pd.read_csv(r"cleaned_dataset\cleaned_exchangerate_dataset.csv")

sales_data['currency_date'] = sales_data['Order Date'] + '_' + sales_data['Currency Code']

exchange_data['currency_date'] = exchange_data['Date'] + '_' + exchange_data['Currency Code']

sales_exchange_data = pd.merge(sales_data, exchange_data, on='currency_date')

sales_exchange_data.drop(['Currency Code_x', 'currency_date'], axis=1, inplace=True)
sales_exchange_data.to_csv("merged_dataset\sales_exchange_data.csv", index=False)
