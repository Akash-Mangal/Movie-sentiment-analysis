
import streamlit as st


st.set_page_config(layout="wide")
choice=st.cache()
#st.title(PROJECT_NAME)
with st.container():
    st.write('<style>body { font-family: sans-serif;border-style: } .header{border-bottom-style: solid;padding-left:10px; padding-right: 800px;z-index: 1; background: White; color: #F63366; position:fixed;top:20px;} .sticky { position: fixed;top: 90; } </style><div class="header" id="myHeader"><h2 style="color: #F63366;"><b>'+"Movie Sentiment Analysis"+'</b></h2></div>', unsafe_allow_html=True)


