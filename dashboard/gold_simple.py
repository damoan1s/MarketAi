#!/usr/bin/env python3
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

st.set_page_config(page_title="MarketAi – Gold", layout="wide")
st.title("MarketAi – Gold Futures vs Spot")

# قراءة البيانات
futures = pd.read_csv("data/gold/futures_1h.csv", index_col=0, parse_dates=True)
spot    = pd.read_csv("data/gold/spot_1h.csv", index_col=0, parse_dates=True)

# آخر 500 شمعة فقط
futures = futures.tail(500)
spot    = spot.tail(500)

# رسم الشارتين
fig = make_subplots(rows=2, cols=1, shared_xaxes=True,
                    subplot_titles=("Gold Futures (GC=F)", "Gold Spot (XAUUSD=X)"),
                    vertical_spacing=0.12)

fig.add_trace(go.Candlestick(x=futures.index,
                             open=futures['open'], high=futures['high'],
                             low=futures['low'], close=futures['close'],
                             name="Futures"), row=1, col=1)

fig.add_open=spot['open'], high=spot['high'],
low=spot['low'], close=spot['close'],trace(go.Candlestick(x=spot.index,
                             open=spot['Open'], high=spot['High'],
                             low=spot['Low'], close=spot['Close'],
                             name="Spot"), row=2, col=1)

fig.update_layout(height=800, title_text="MarketAi – أول داشبورد ناجح")
st.plotly_chart(fig, use_container_width=True)

st.success("الداشبورد شغال 100% – MarketAi بدأ يتنفس!")
