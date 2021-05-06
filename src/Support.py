# @author: Renan Silva
#? @github: https://github.com/rfelipesilva
#! Python3.8

import pandas as pd

class Data:
    """Class to centralize and provide any kind of data/path/credentials
    """

    def __init__(self):
        pass
    
    def get_stocks_list(self):
        
        stocks_list = pd.read_csv('data/bra_stocks_list.csv', delimiter = '|', encoding = 'utf-8')
        return list(stocks_list['Symbol'].sort_values(ascending = True))

    def get_language_dict(self):

        language_dict = {
            'pt' : {
                'language' : 'pt',
                'sidebar' : {
                    'period' : {
                        'header' : 'Seleção',
                        'title' : 'Selecione o período:',
                        'values' : {
                            '1 Mês' : '1mo',
                            '3 Meses' : '3mo',
                            '6 Meses' : '6mo',
                            '1 Ano' : '1y'
                        }
                    },
                    'stocks' : {
                        'title' : 'Selecione as ações que deseja comparar:'
                    }
                },
                'body' : {
                    'description' : 'Stocker faz comparações entre ações parecer fácil, dá uma chance!' 
                }

            },
            'en': {
                'language' : 'en',
                'sidebar' : {
                    'period' : {
                        'header' : 'Selection',
                        'title' : 'Select period:',
                        'values' : {
                            '1 Month' : '1mo',
                            '3 Months' : '3mo',
                            '6 Months' : '6mo',
                            '1 Year' : '1y'
                        }
                    },
                    'stocks' : {
                        'title' : 'Select the stocks you want to compare:'
                    }
                },
                'body' : {
                    'description' : 'Stocker makes comparisons between stocks look easy, give it a try!'
                }
            }
        }

        return language_dict