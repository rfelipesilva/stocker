# @author: Renan Silva
#? @github: https://github.com/rfelipesilva
#! Python3.8

from pandas_datareader import data as pdr

stock_code = 'PETR4.SA'

# stock = yf.Ticker(stock_code) # MM - DD - YYYY
# stock = pdr.DataReader(stock_code, data_source='yahoo', start=f'10-5-2022', end='10-5-2022')

# print(stock['Close'])

stock = pdr.DataReader('PETR4.SA', data_source='yahoo', start='10-1-2022', end='10-5-2022')
print(stock['Close'])