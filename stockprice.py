#!/usr/bin/env python
# coding: utf-8

# In[5]:


import streamlit as st
import pandas as pd
import yfinance as yf

st.write("""
# simple stock price app

shown are the stock **closing price** and **volume** of google

""")
#select the stock
tickersymbol='GOOGL'
#get data
tickerData=yf.Ticker(tickersymbol)
#get historical data
tickerdf=tickerData.history(period='1d',start='2010-5-31',end='2020-8-28')

st.write("""
## closing price
""")
st.line_chart(tickerdf.Close)

st.write("""
## volume price
""")

st.line_chart(tickerdf.Volume)








# In[ ]:




