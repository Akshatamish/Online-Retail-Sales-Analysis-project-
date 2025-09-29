import pandas as pd
import matplotlib.pyplot as plt

#Load Clean Dataset
df=pd.read_excel("data.xlsx")
# print(df.head())

# ------------------------------
# Sales Overview
# ------------------------------
total_revenue=df['Total Price'].sum()
total_transaction=df['InvoiceNo'].nunique()
Total_Customer=df['CustomerID'].nunique()

print("Total Revenue",total_revenue)
print("Total Transaction", total_transaction)
print("Total Customer", Total_Customer)

# ------------------------------
# Trends: Revenue by Month, Week, Day
# ------------------------------

df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

#Revenue by Month
monthly_Revenue=df.groupby(df['InvoiceDate'].dt.to_period("M"))['Total Price'].sum()

#Revenue by week
weekly_Revenue=df.groupby(df['InvoiceDate'].dt.to_period("W"))['Total Price'].sum()

#Revenue by Day
daily_Revenue=df.groupby(df['InvoiceDate'].dt.date)['Total Price'].sum()

# ------------------------------
# Top Performers
# ------------------------------
# Top 10 Products by Revenue

top_product=df.groupby(df['Description'])['Total Price'].sum().nlargest(10)

#Top 10 Customer
top_customer=df.groupby(df['CustomerID'])['Total Price'].sum().nlargest(10)

#Top 10 Country by Revenue

top_countries=df.groupby(['Country'])['Total Price'].sum().nlargest(10)

# ------------------------------
# Visualization
# ------------------------------

#Line Plot--- Monthly Revenue
monthly_Revenue.plot(kind='line',figsize=(10,5),linewidth=2,marker='o',label='Monthly Revenue')
plt.ylabel("Revenue")
plt.xlabel("Month")
plt.title("Monthly Sales VS Revenue Chart")
plt.show()

#Line plot --- Daily Revenue

daily_Revenue.plot(kind='line', figsize=(10,5), title="Daily Revenue")
plt.ylabel("Revenue")
plt.xlabel("Date")
plt.show()

# Bar Chart - Top 10 Products
top_product.plot(kind='bar',color='orange',figsize=(10,6))
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.title("Top 10 Product By Revenue")
plt.show()

# Bar Chart - Top 10 Customers
top_customer.plot(kind='bar', figsize=(10,5), title="Top 10 Customers by Revenue")
plt.ylabel("Revenue")
plt.show()

# Pie Chart - Top 10 Countries
top_countries.plot(kind='pie', autopct='%1.1f%%', figsize=(8,8), title="Top Countries by Revenue")
plt.show()
