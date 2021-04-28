# -*- coding: utf-8 -*-
#! Python3.8
#? @author: Renan Silva
#? @github: https://github.com/rfelipesilva

import pandas as pd
import streamlit as st

from Config import Data

st.title('Stock Analyzer')

st.markdown("""
Stock Analyzer makes comparisons between stocks look easy, give it a try!
""")

stocks_list = Data().get_stocks_list()

st.sidebar.header('Selection')
selected_period = st.sidebar.selectbox('Period:', ['1mo', '3mo', '6mo', '1y'])

selected_stocks = st.sidebar.multiselect('Stocks', stocks_list)

#! TO DO:
#@st.cache
#def load_data