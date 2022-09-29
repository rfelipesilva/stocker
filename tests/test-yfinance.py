# import yfinance as yf
import pandas as pd
from pandas_datareader import data as pdr

stock_code = 'PETR4.SA'

# stock = yf.Ticker(stock_code)
stock = pdr.DataReader(stock_code, data_source='yahoo', start=f'02-20-2020', end='02-20-2021')

print(stock)