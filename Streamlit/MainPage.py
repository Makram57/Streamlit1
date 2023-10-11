import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.figure_factory as ff
import plotly.express as px
import chart_studio.plotly as py
from dash import Dash, dcc, html, Input, Output
import streamlit as st
st.set_page_config(page_title="Multiple Plots")

st.title("Main Page  😃")
st.sidebar.success("Select a page")
st.markdown('<span style="color: #333; text-align: center;font-size: 25px;">🚀 Welcome to My Streamlit App! 🚀 </span>',unsafe_allow_html=True)
st.markdown("<span style='font-size: 25px;'>In this Interface we you will be seing 2 plots using streamlit</span>", unsafe_allow_html=True)

