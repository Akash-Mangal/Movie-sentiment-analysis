
import streamlit as st
from config import *

st.set_page_config(layout="wide")
choice=st.cache()
#st.title(PROJECT_NAME)
with st.container():
    st.write('<style>body { font-family: sans-serif;border-style: } .header{border-bottom-style: solid;padding-left:10px; padding-right: 800px;z-index: 1; background: White; color: #F63366; position:fixed;top:20px;} .sticky { position: fixed;top: 20; } </style><div class="header" id="myHeader"><h2 style="color: #F63366;"><b>'+"Movie Sentiment Analysis"+'</b></h2></div>', unsafe_allow_html=True)
with st.container():
   img_col=st.columns((4,2,3))
    img_col[0].image('download.jpg',use_column_width=True)
    #img_col[0].write(ABOUT)

    
