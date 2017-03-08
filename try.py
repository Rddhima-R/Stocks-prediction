import pandas as pd 
import quandl
import matplotlib.pyplot as plt
start_date='2016-01-01'
end_date='2017-01-31'

data=pd.date_range(start_date,end_date)

df1=pd.DataFrame(index=data)

symbols=['GOOGL','AAPL','FB']

for symbol in symbols:
	data1= quandl.get("WIKI/{}".format(symbol),index='Date', parse_dates=True,usecols=['Date', 'Adj. Close'], na_values=['nan'])
	data1=data1[['Adj. Close']]
	data1=data1.rename(columns={'Adj. Close':symbol})
	df1=df1.join(data1)
	df1=df1.dropna()
df2=df1.copy()
df2[1:]=(df1[1:]/df1[:-1].values)-1
df2.ix[0,:]=0
print df2['AAPL'].kurtosis()
df2['AAPL'].plot()
plt.show()
