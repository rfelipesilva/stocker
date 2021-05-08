# @author: Renan Silva
#? @github: https://github.com/rfelipesilva
#! Python3.8

import os
import pandas as pd
import streamlit as st
import yfinance as yf
import plotly.express as px

from Support import Data

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

file_dir = '{}\\src\\style.css'.format(os.path.abspath(os.getcwd()))
# print(file_dir)

local_css(file_dir)

# @st.cache
def load_data(stock_symbol_list, period_interval, language):

    """Provide stocks information to plot

    Args:
        stock_symbol_list (list): Multiselect option coming from "selected_stocks" variable
        period_interval (string): Selectbox option coming from "selected_period" variable

    Returns:
        DataFrame: pandas dataframe with day as index, Close as price and Stocks as legend to use in the plotly
    """

    df_to_concactenate = []
    for each_stock in stock_symbol_list:
        stock_info = yf.Ticker(each_stock).history(period = period_interval)
        stock_info['Stock'] = each_stock
        df_to_concactenate.append(stock_info)
        
    stocks_df = pd.concat(df_to_concactenate)

    if language == 'pt':
        stocks_df.rename(columns = {'Close' : 'Preço', 'Stock' : 'Ações'}, inplace = True)
        return stocks_df[['Preço', 'Ações']]
    else:
        stocks_df.rename(columns = {'Close' : 'Price', 'Stock' : 'Stocks'}, inplace = True)
        return stocks_df[['Price', 'Stocks']]

language = Data.get_language_dict()
stocks_list = Data.get_stocks_list()

def update_page(language_dict):

    """Update page according with specific language dicionary

    Args: language_dict (dictionary): Radio button option comingo from "selected_language" variable

    Returns: updated page according with user language selected
    """

    st.sidebar.header(language_dict['sidebar']['period']['header'])
    selected_period = st.sidebar.selectbox(language_dict['sidebar']['period']['title'], list(language_dict['sidebar']['period']['values'].keys()))
    selected_stocks = st.sidebar.multiselect(language_dict['sidebar']['stocks']['title'], stocks_list)

    st.sidebar.header(language_dict['sidebar']['about']['header'])
    st.sidebar.info('{}'.format(language_dict['sidebar']['about']['text']))

    st.title('Stocker')

    st.markdown("""{}""".format(language_dict['body']['description']))

    if selected_stocks:
        period = language_dict['sidebar']['period']['values'][selected_period]
        data_to_plot = load_data(selected_stocks, period, language_dict['language'])
        fig = px.line(data_to_plot, x = data_to_plot.index, y = data_to_plot.columns[0], color = data_to_plot.columns[1])
        st.plotly_chart(fig)
    else:
        st.info(language_dict['body']['message_before_selection'])
    

st.sidebar.header('Language/Idioma')
selected_language = st.sidebar.radio('', ['Portuguese/Português', 'English/Inglês'])

if selected_language == 'Portuguese/Português':
    update_page(language['pt'])
else:
    update_page(language['en'])