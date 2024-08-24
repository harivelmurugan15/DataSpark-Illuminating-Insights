import mysql.connector
import pandas as pd

con = mysql.connector.connect(
    host="Provide your hostname here",
    user="Provide your username here",
    password="Provide your password here",
    database="Provide your database name here"
)

cursor = con.cursor()

query1 = """SELECT Product_Key,Product_Name, COUNT(*) as element_count FROM sales_product GROUP BY Product_Key,
            Product_Name order by element_count desc limit 10;"""
df = pd.DataFrame()

product_key = []
product_name = []
sold_count = []

cursor.execute(query1)

for i in cursor:
    product_key.append(i[0])
    product_name.append(i[1])
    sold_count.append(i[2])

df['product_key'] = product_key
df['product_name'] = product_name
df['sold_count'] = sold_count

df.to_csv("extracted data\Top_10_Most_sold.csv", index=False)

query2 = """SELECT Product_Key,Product_Name, COUNT(*) as element_count FROM sales_product GROUP BY Product_Key,
            Product_Name order by element_count asc limit 10;"""
df = pd.DataFrame()

product_key = []
product_name = []
sold_count = []

cursor.execute(query2)

for i in cursor:
    product_key.append(i[0])
    product_name.append(i[1])
    sold_count.append(i[2])

df['product_key'] = product_key
df['product_name'] = product_name
df['sold_count'] = sold_count

df.to_csv("extracted data\Ten_Least_sold.csv", index=False)

query3 = """select Product_Key,Product_Name,(Quantity*Unit_Price_USD)-(Quantity*Unit_Cost_USD) 
                as profit from mde92.sales_product order by profit desc limit 10 ;"""
df = pd.DataFrame()
product_key = []
product_name = []
profit = []

cursor.execute(query3)

for i in cursor:
    product_key.append(i[0])
    product_name.append(i[1])
    profit.append(i[2])

df['product_key'] = product_key
df['product_name'] = product_name
df['profit'] = profit

df.to_csv("extracted data\Ten_Most_Profitable_products.csv", index=False)

query4 = """select Product_Key,Product_Name,(Quantity*Unit_Price_USD)-(Quantity*Unit_Cost_USD) 
                as profit from mde92.sales_product order by profit asc limit 10 ;"""

product_key = []
product_name = []
profit = []

cursor.execute(query4)
df = pd.DataFrame()
for i in cursor:
    product_key.append(i[0])
    product_name.append(i[1])
    profit.append(i[2])

df['product_key'] = product_key
df['product_name'] = product_name
df['profit'] = profit

df.to_csv("extracted data\Ten_Least_Profitable_products.csv", index=False)

query5 = """SELECT Customer_Key,Name,city,COUNT(*) AS visit_count FROM sales_customer group by Customer_Key,
                Name,city order by visit_count desc Limit 10;"""

customer_key = []
name = []
city = []
visited = []

cursor.execute(query5)
df = pd.DataFrame()

for i in cursor:
    customer_key.append(i[0])
    name.append(i[1])
    city.append(i[2])
    visited.append(i[3])

df['customer_key'] = customer_key
df['Name'] = name
df['City'] = city
df['Visited'] = visited

df.to_csv("extracted data\Most_visited_Customer.csv", index=False)

query6 = "SELECT Gender, count(*) as Gender_Count FROM customers group by Gender;"

gender = []
gender_count = []

cursor.execute(query6)
df = pd.DataFrame()

for i in cursor:
    gender.append(i[0])
    gender_count.append(i[1])

df['Gender'] = customer_key
df['Gender_Count'] = name

df.to_csv("extracted data\Gender_biased_Customer.csv", index=False)

query7 = """SELECT Store_Key,State, sum(Quantity) as total_quantity FROM sales_store group by Store_Key,
            State order by total_quantity desc limit 3;"""

store_key = []
state = []
total_quantity = []

df = pd.DataFrame()

cursor.execute(query7)

for i in cursor:
    store_key.append(i[0])
    state.append(i[1])
    total_quantity.append(i[2])

df['store_key'] = store_key
df['state'] = state
df['total_quantity'] = total_quantity

df.to_csv("extracted data\Most_sold_stores.csv", index=False)

query8 = """(SELECT * FROM exchanges where Currency_Code = 'AUD' order by Exchange desc limit 2) union 
            (SELECT * FROM exchanges where Currency_Code = 'USD' order by Exchange desc limit 2) union
            (SELECT * FROM exchanges where Currency_Code = 'GBP' order by Exchange desc limit 2) union
            (SELECT * FROM exchanges where Currency_Code = 'CAD' order by Exchange desc limit 2) union
            (SELECT * FROM exchanges where Currency_Code = 'EUR' order by Exchange desc limit 2);"""

date = []
currency_code = []
exchange = []

df = pd.DataFrame()

cursor.execute(query8)

for i in cursor:
    date.append(i[0])
    currency_code.append(i[1])
    exchange.append(i[2])

df['Date'] = date
df['Currency_code'] = currency_code
df['Exchange'] = exchange

df.to_csv("extracted data\Highest_Exchange_values.csv", index=False)

query9 = """SELECT Order_Number,Product_Key,Quantity,Product_Name, (Quantity*Unit_Price_USD) as Total_sales 
            FROM mde92.sales_product where year(Order_Date) = 2016;"""


Order_Number = []
Product_Key = []
Quantity = []
Product_Name = []
Total_sales = []

df = pd.DataFrame()

cursor.execute(query9)

for i in cursor:
    Order_Number.append(i[0])
    Product_Key.append(i[1])
    Quantity.append(i[2])
    Product_Name.append(i[3])
    Total_sales.append(i[4])


df['Order_Number'] = Order_Number
df['Product_Key'] = Product_Key
df['Quantity'] = Quantity
df['Product_Name'] = Product_Name
df['Total_sales'] = Total_sales


df.to_csv("extracted data\Total_2016_sales_values.csv", index=False)

query10 = """SELECT * FROM stores where Square_Meters > 2000"""


store_key = []
country = []
state = []
sq_meter = []
open_date = []

df = pd.DataFrame()

cursor.execute(query10)

for i in cursor:
    store_key.append(i[0])
    country.append(i[1])
    state.append(i[2])
    sq_meter.append(i[3])
    open_date.append(i[4])


df['store_key'] = store_key
df['country'] = country
df['state'] = state
df['sq_meter'] = sq_meter
df['open_date'] = open_date


df.to_csv("extracted data\Largest_stores.csv", index=False)
