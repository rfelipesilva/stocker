#? @author: Renan Silva
#? @github: https://github.com/rfelipesilva
#! Python3.8

import pandas as pd
import streamlit as st
import yfinance as yf
import plotly.express as px

from Support import Data

@st.cache
def load_data(stock_symbol_list, period_interval):

    """Provide stocks information to plot

    Args:
        stock_symbol_list (list): Multiselect option coming from "selected_stocks" variable
        period_interval (string): Selectbox option coming from "selected_period" variable

    Returns:
        DataFrame: pandas dataframe with day as index, Close as price and Stocks as legend to use in the plotly
    """

    df_to_concactenate = []
    for each_stock in stock_symbol_list:
        period_value = Data().get_period_dict(period_interval)
        stock_info = yf.Ticker(each_stock).history(period = period_value)
        stock_info['Stock'] = each_stock
        df_to_concactenate.append(stock_info)
        
    stocks_df = pd.concat(df_to_concactenate)
    stocks_df.rename(columns={'Close' : 'Price'}, inplace = True)
    return stocks_df[['Price', 'Stock']]

st.title('Stock Analyzer')

st.markdown("""
Stock Analyzer makes comparisons between stocks look easy, give it a try!
""")

stocks_list = Data().get_stocks_list()

st.sidebar.header('Selection')
selected_period = st.sidebar.selectbox('Period:', ['1 Month', '3 Months', '6 Months', '1 Year'])

selected_stocks = st.sidebar.multiselect('Stocks', stocks_list)

if selected_stocks:
    to_plot = load_data(selected_stocks, selected_period)
    fig = px.line(to_plot, x = to_plot.index, y = 'Price', color = 'Stock')
    st.plotly_chart(fig)