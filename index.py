import pandas as pd

df=pd.read_excel("Online Retail.xlsx")
# print(df.isnull().sum())  to find null value
df.dropna(inplace=True)   #clean null value
print(df)

# Remove canceled orders (InvoiceNo starts with 'C')
df = df[~df['InvoiceNo'].astype(str).str.startswith('C')]

# print(df.head())


#  Remove negative or zero Quantity and UnitPrice
df = df[(df['Quantity'] > 0) & (df['UnitPrice'] > 0)]
# print("After removing negative/zero Quantity or UnitPrice:", df.shape)

#Create a columns Total Revenue
df['Total Price'] = df['Quantity']*df['UnitPrice']

df.to_excel("Data.xlsx",index="False")


