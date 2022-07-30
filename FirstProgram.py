
import pandas as pd
import yfinance as yf
import numpy as np
import datetime as dt
from pandas_datareader import data as pdr


print("- Stock Average Volume Search")

stock = input(" Enter Stock Ticker: ")
print(stock)
n = input("Enter Date Range: ")
print(n)

end_date = dt.datetime.now().date()
start_date = pd.to_datetime('today') - pd.Timedelta(int(n), unit='D')
df = pdr.get_data_yahoo(stock, start_date, end_date)

df = df["Volume"].mean()

print(" Average Daily Volume For yor date range")
print(df)
