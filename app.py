
import streamlit as st
from config import *

st.set_page_config(layout="wide")
choice=st.cache()
#st.title(PROJECT_NAME)
with st.container():
    st.write('<style>body { font-family: sans-serif;border-style: } .header{border-bottom-style: solid;padding-left:10px; padding-right: 800px;z-index: 1; background: White; color: #F63366; position:fixed;top:20px;} .sticky { position: fixed;top: 20; } </style><div class="header" id="myHeader"><h2 style="color: #F63366;"><b>'+"Movie Sentiment Analysis"+'</b></h2></div>', unsafe_allow_html=True)
with st.container():
    cols=st.columns(6)
    
a=cols[0].button(MENU_OPTION[0])
b=cols[1].button(MENU_OPTION[1])
c=cols[2].button(MENU_OPTION[2])
d=cols[3].button(MENU_OPTION[3])
e=cols[4].button(MENU_OPTION[4])
f=cols[5].button(MENU_OPTION[5])

