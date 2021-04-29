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