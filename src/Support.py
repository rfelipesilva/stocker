#! Python3.8
#? @author: Renan Silva
#? @github: https://github.com/rfelipesilva

import pandas as pd

class Data:
    """Class to centralize and provide any kind of data/path/credentials
    """

    def __init__(self):
        pass
    
    def get_stocks_list(self):
        
        stocks_list = pd.read_csv('data/bra_stocks_list.csv', delimiter = '|', encoding = 'utf-8')
        return list(stocks_list['Symbol'].sort_values(ascending = True))

    def get_period_dict(self, period_value):

        period_dict = {
            '1 Month' : '1mo',
            '3 Months' : '3mo',
            '6 Months' : '6mo',
            '1 Year' : '1y'
        }

        return period_dict[period_value]