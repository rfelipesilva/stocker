#? @author: Renan Silva
#? @github: https://github.com/rfelipesilva
#! Python3.8

import pandas as pd
import streamlit as st
import yfinance as yf
import plotly.express as px

from Config import Data

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
        stock_info = yf.Ticker(each_stock).history(period = period_interval)
        stock_info['Stock'] = each_stock
        df_to_concactenate.append(stock_info)
        
    stocks_df = pd.concat(df_to_concactenate)
    return stocks_df[['Close', 'Stock']]

st.title('Stock Analyzer')

st.markdown("""
Stock Analyzer makes comparisons between stocks look easy, give it a try!
""")

stocks_list = Data().get_stocks_list()

st.sidebar.header('Selection')
selected_period = st.sidebar.selectbox('Period:', ['1mo', '3mo', '6mo', '1y'])

selected_stocks = st.sidebar.multiselect('Stocks', stocks_list)

st.markdown("""

""")

if selected_stocks:
    to_plot = load_data(selected_stocks, selected_period)

    fig = px.line(to_plot, x = to_plot.index, y = 'Close', color = 'Stock')

    st.plotly_chart(fig)