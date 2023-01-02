# @author: Renan Silva
#? @github: https://github.com/rfelipesilva
#! Python3.8

from pandas_datareader import data as pdr
import yfinance as yf

yf.pdr_override()

stock_code = 'PETR4.SA'

# stock = yf.Ticker(stock_code) # MM - DD - YYYY
# stock = pdr.DataReader(stock_code, data_source='yahoo', start=f'10-5-2022', end='10-5-2022')

# print(stock['Close'])
# old
# stock = pdr.DataReader(['PETR4.SA'], data_source='yahoo', start='10-1-2022', end='10-5-2022')

# added yfinance again
# new
stock = pdr.get_data_yahoo('ITSA4.SA', start='2022-12-26', end='2022-12-30')
# print(stock['Close'])
print(stock)