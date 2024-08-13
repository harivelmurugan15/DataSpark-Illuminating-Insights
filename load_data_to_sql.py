import mysql.connector
import pandas as pd


def find_values(df):
    x = ""
    row = df.iloc[0].values
    for i in row:
        x += "%s,"
    x = x[:-1]
    return x


con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="MDE92"
)

cursor = con.cursor()
# sales table

sales_data = pd.read_csv("cleaned_sales_dataset.csv",parse_dates=['Order Date','Delivery Date'])

create_query = """create table if not exists sales(Order_Number int,Line_Item int,Order_Date datetime,Delivery_Date datetime,
            Customer_Key int,Store_Key int,Product_Key int,Quantity int,Currency_Code varchar(10))"""

cursor.execute(create_query)

insert_query = "insert into sales values("+find_values(sales_data)+")"


for index in sales_data.index:
    row = sales_data.iloc[index].values
    val = [int(row[0]),int(row[1]),str(row[2]),str(row[3]),int(row[4]) ,int(row[5]),int(row[6]),int(row[7]),str(row[8])]
    cursor.execute(insert_query,val)
    con.commit()

# customer table

customer_data = pd.read_csv(r"cleaned_customer_dataset.csv", encoding='latin1', parse_dates=['Birthday'])

create_query = """create table if not exists customers(CustomerKey INT ,Gender VARCHAR(10),Name VARCHAR(100), 
                    City VARCHAR(100),stateCode VARCHAR(110),State VARCHAR(100),ZipCode VARCHAR(20),Country VARCHAR(100), 
                    Continent VARCHAR(100),Birthday DATETIME,Age INT)"""

cursor.execute(create_query)
insert_query = "insert into customers values(" + find_values(customer_data) + ")"
print(insert_query)


for index in customer_data.index:
    row = customer_data.iloc[index].values
    val = [int(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]),
           str(row[8]), str(row[9]), int(row[10])]
    cursor.execute(insert_query, val)
    con.commit()

# product data

product_data = pd.read_csv(r"cleaned_product_dataset.csv")

create_query = """create table if not exists products(ProductKey int,Product_Name varchar(160),Brand varchar(60),
                  Color varchar(60),Unit_Cost_USD decimal(20,2),Unit_Price_USD decimal(20,2) ,SubcategoryKey int,
                  Subcategory varchar(60),CategoryKey int,Category varchar(60))"""

cursor.execute(create_query)
insert_query = "insert into products values(" + find_values(product_data) + ")"
print(insert_query)


for index in product_data.index:
    row = product_data.iloc[index].values
    val = [int(row[0]), str(row[1]), str(row[2]), str(row[3]), float(row[4]), float(row[5]), int(row[6]), str(row[7]),
           int(row[8]), str(row[9])]
    cursor.execute(insert_query, val)
    con.commit()

# store data

store_data = pd.read_csv(r"cleaned_stores_dataset.csv")

create_query = """create table if not exists stores(StoreKey int,Country varchar(100),State varchar(100)
                    ,Square_Meters decimal(20,2),Open_Date datetime)"""

cursor.execute(create_query)
insert_query = "insert into stores values(" + find_values(store_data) + ")"
print(insert_query)


for index in store_data.index:
    row = store_data.iloc[index].values
    val = [int(row[0]), str(row[1]), str(row[2]),float(row[3]),str(row[4])]
    cursor.execute(insert_query, val)
    con.commit()

# exchange data

exchange_data = pd.read_csv(r"cleaned_exchangerate_dataset.csv")

create_query = """create table if not exists exchanges(Date varchar(60),Currency_Code varchar(100),Exchange decimal(20,3))"""

cursor.execute(create_query)
insert_query = "insert into exchanges values(" + find_values(exchange_data) + ")"
print(insert_query)


for index in exchange_data.index:
    row = exchange_data.iloc[index].values
    val = [str(row[0]), str(row[1]), float(row[2])]
    cursor.execute(insert_query, val)
    con.commit()

# sale_customer_data

sale_customer_dataset = pd.read_csv(r"sales_customer_data.csv")

create_query = """create table if not exists Sales_customer(Order_Number int,Line_Item int,Order_Date datetime
                    ,Delivery_Date datetime,Customer_Key int,Store_Key int,Product_Key int,Quantity int,
                    Currency_Code varchar(10),Gender VARCHAR(10),Name VARCHAR(100),City VARCHAR(100),
                    stateCode VARCHAR(110),State VARCHAR(100),ZipCode VARCHAR(20),Country VARCHAR(100),
                     Continent VARCHAR(100),Birthday DATETIME,Age INT)"""

cursor.execute(create_query)
insert_query = "insert into Sales_customer values(" + find_values(sale_customer_dataset) + ")"
print(insert_query)

for index in sale_customer_dataset.index:
    row = sale_customer_dataset.iloc[index].values
    val = [int(row[0]), int(row[1]), str(row[2]), str(row[3]), int(row[4]), int(row[5]), int(row[6]), int(row[7]),
           str(row[8]),str(row[9]), str(row[10]), str(row[11]), str(row[12]), str(row[13]), str(row[14]), str(row[15]),
           str(row[16]),str(row[17]), int(row[18])]
    cursor.execute(insert_query, val)
    con.commit()

# sale_product dataset

sale_product_dataset = pd.read_csv(r"sales_product_data.csv")

create_query = """create table if not exists Sales_product(Order_Number int,Line_Item int,Order_Date datetime,
                  Delivery_Date datetime,Customer_Key int,Store_Key int,Product_Key int,Quantity int,
                  Currency_Code varchar(10),Product_Name varchar(160),Brand varchar(60), Color varchar(60),
                  Unit_Cost_USD decimal(20,2),Unit_Price_USD decimal(20,2) ,SubcategoryKey int,Subcategory varchar(60),
                  CategoryKey int,Category varchar(60))"""

cursor.execute(create_query)
insert_query = "insert into Sales_product values(" + find_values(sale_product_dataset) + ")"
print(insert_query)

for index in sale_product_dataset.index:
    row = sale_product_dataset.iloc[index].values
    val = [int(row[0]), int(row[1]), str(row[2]), str(row[3]), int(row[4]), int(row[5]), int(row[6]), int(row[7]),
           str(row[8]), str(row[9]), str(row[10]), str(row[11]), float(row[12]), float(row[13]), int(row[14]),
           str(row[15]), int(row[16]), str(row[17])]
    cursor.execute(insert_query, val)
    con.commit()

# sales_store_dataset

sale_store_dataset = pd.read_csv(r"sales_store_data.csv")

create_query = """create table if not exists Sales_store(Order_Number int,Line_Item int,Order_Date datetime,
                  Delivery_Date datetime,Customer_Key int,Store_Key int,Product_Key int,Quantity int,
                  Currency_Code varchar(10),Country varchar(100),State varchar(100)
                    ,Square_Meters decimal(20,2),Open_Date datetime)"""

cursor.execute(create_query)
insert_query = "insert into Sales_store values(" + find_values(sale_store_dataset) + ")"
print(insert_query)

for index in sale_store_dataset.index:
    row = sale_store_dataset.iloc[index].values
    val = [int(row[0]), int(row[1]), str(row[2]), str(row[3]), int(row[4]), int(row[5]), int(row[6]), int(row[7]),
           str(row[8]), str(row[9]), str(row[10]), float(row[11]), str(row[12])]
    cursor.execute(insert_query, val)
    con.commit()

# sales_exchange

sales_exchange_data = pd.read_csv(r"sales_exchange_data.csv")

create_query = """create table if not exists sales_exchange(Order_Number int,Line_Item int,Order_Date datetime, 
                    Delivery_Date datetime, Customer_Key int,Store_Key int,Product_Key int,Quantity int,
                    Date datetime,Currency varchar(10),Exchange decimal(20,4))"""

cursor.execute(create_query)
insert_query = "insert into sales_exchange values(" + find_values(sales_exchange_data)+ ")"
print(insert_query)

for index in sales_exchange_data.index:
    row = sales_exchange_data.iloc[index].values
    val = [int(row[0]), int(row[1]), str(row[2]), str(row[3]), int(row[4]), int(row[5]), int(row[6]),
           int(row[7]), str(row[8]), str(row[9]), float(row[10])]
    cursor.execute(insert_query, val)
    con.commit()
