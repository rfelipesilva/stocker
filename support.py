# @author: Renan Silva
#? @github: https://github.com/rfelipesilva
#! Python3.8

import pandas as pd

class Data:
    """Class to centralize and provide any kind of data/path/credentials
    """
    
    def get_stocks_list():
        stocks_list = pd.read_csv('data/bra_stocks_list.csv', delimiter = '|', encoding = 'utf-8')
        return list(stocks_list['Symbol'].sort_values(ascending = True))

    def get_language_dict():
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
                    },
                    'about' : {
                        'header' : 'Sobre',
                        'text' : '''
                            **Stocker** é um aplicativo desenvolvido por *Renan Silva* que busca facilitar a comparação entre ações da bolsa de valores do Brasil (B3).
                            \nGostaria de sugerir melhorias ou comentar sobre o aplicativo? Esses são os canais onde você pode entrar em contato:
                            \n![LinkedIn](https://raw.githubusercontent.com/paulrobertlloyd/socialmediaicons/main/linkedin-16x16.png) [LinkedIn perfil](https://www.linkedin.com/in/renan-silva-16960313a/?locale=en_US)
                            \n![GitHub](https://raw.githubusercontent.com/paulrobertlloyd/socialmediaicons/main/github-16x16.png) [GitHub repositório](https://github.com/rfelipesilva/webapp-stocker-python38)
                        '''
                    }
                },
                'body' : {
                    'description' : 'Stocker faz comparações entre ações parecer fácil, dá uma chance!',
                    'message_before_selection' : '''
                        Para obter o gráfico, do lado esquerdo :arrow_left: do aplicativo na seção **Seleção**, selecione as ações e o período desejado. :chart_with_upwards_trend:
                    '''
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
                    },
                    'about' : {
                        'header' : 'About',
                        'text' : '''
                            **Stocker** is an app developed by *Renan Silva* that aims to facilitate the stocks comparison of Brazil stock exchange (B3).
                            \nWould you like to share your comments or suggest improvements? Here are the channels to contact:
                            \n![LinkedIn](https://raw.githubusercontent.com/paulrobertlloyd/socialmediaicons/main/linkedin-16x16.png) [LinkedIn profile](https://www.linkedin.com/in/renan-silva-16960313a/?locale=en_US)
                            \n![GitHub](https://raw.githubusercontent.com/paulrobertlloyd/socialmediaicons/main/github-16x16.png) [GitHub repository](https://github.com/rfelipesilva/webapp-stocker-python38)
                        '''
                    }
                },
                'body' : {
                    'description' : 'Stocker makes comparisons between stocks look easy, give it a try!',
                    'message_before_selection' : '''
                        To get the chart, on the left :arrow_left: side of the app in the **Selection** section, select the stocks and desired period. :chart_with_upwards_trend:
                    '''
                }
            }
        }

        return language_dict
