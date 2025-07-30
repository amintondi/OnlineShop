import pandas as pd
import matplotlib.pyplot as plt
from persiantools.jdatetime import JalaliDate

def convert_date(miladyDate):
    return JalaliDate(miladyDate)

# df = pd.read_excel('Online Retail.xlsx')
# df.to_csv('Online Retail.csv',sep=',')
df=pd.read_csv('Online Retail.csv')

df = df[df['Country'] != 'Israel']
df.dropna(inplace=True)
df['Quantity'].dropna(inplace=True)
df['UnitPrice'].dropna(inplace=True)

df=df[df['Quantity'] > 0]
df=df[df['UnitPrice'] > 0]

#print(df.duplicated().sum())
df.drop_duplicates(inplace=True)
#print(df.duplicated().sum())

#print(df.isnull().sum())
#print(len(df))
#df.info()

# df["PersianDate"] = df["Date"].apply(convert_date)

#تعداد مشتریان به تفکیک کشور
#CustomerIDCount = df.groupby('Country').count()['CustomerID']
# customerPerCountry= df.groupby('Country')['CustomerID'].nunique()
# customerPerCountry.plot(kind='bar',
#     figsize=(14, 6),
#     title='Customers per Country (Log Scale)',
#     xlabel='Country',
#     ylabel='Number of Customers')
# print(customerPerCountry)
# plt.show()

# تعداد کل مشتریان منحصر به فرد
# uniqeCustomerCount = df['CustomerID'].nunique()
# print(uniqeCustomerCount)

# تعداد کل محصولات منحصر به فرد
# uniqeStockCode = df['StockCode'].nunique()
# print(uniqeStockCode)

# میزان فروش هر کالا به تفکیک کشور
df['TotalPrice']=df['Quantity']*df['UnitPrice']
totalProductPrice=df.groupby(['StockCode','Country'])['TotalPrice'].sum()
totalProductPrice.sort_values(ascending=False, inplace=True)
totalProductPrice.to_csv('totalPrice.csv')
