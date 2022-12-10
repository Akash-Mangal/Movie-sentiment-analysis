
import streamlit as st
import re
import pickle
from config import*
import matplotlib.pyplot as plt


def clean(x):
    #x=re.sub(r'\W',' ',x)
    #x = re.sub(r'[^a-zA-Z]',' ',x)
    x = re.sub("wouldn\'t",'would not',x)
    x = re.sub("they \ 've",'they have',x)
    
    #to remove html tags
    x = re.sub(r'<.*?>', '', x)
    
    #to remove everything except alpha
    x = re.sub(r'[^a-zA-Z]',' ',x)
     
    x = re.sub(r'\s+',' ',x)          #remove extra space's
    return x.lower()

st.set_page_config(layout="wide")
choice=st.cache()
#st.title(PROJECT_NAME)
with st.container():
    st.write('<style>body .sticky{ font-family: sans-serif;border-style: } .header{border-bottom-style: solid;padding-left:10px; padding-right: 800px;z-index: 1; background: White; color: #F63366; position:fixed;top:20px;} .sticky { position: fixed;top: 20; } </style><div class="header" id="myHeader"><h2 style="color: #F63366;"><b>'+"Movie Sentiment Analysis"+'</b></h2></div>', unsafe_allow_html=True)


with st.container():
   img_col=st.columns((1,2,1))
   img_col[0].image("data:image/jpeg;base64,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",use_column_width=True)
   inp=img_col[1].text_input("",placeholder="Add Comment")
   a=0
   for i in coment:
     a+=1
     img_col[1].write(a) 
     img_col[1].write(i)

f=[]
#f.append(inp)
#inp=clean(f[0])

for i in coment:
    d=clean(i)
    f.append(d)
   
with open("cv1.pkl",'rb') as f1:
    cv1=pickle.load(f1)

t=cv1.transform(f).toarray()

with open("nb_model.pkl",'rb') as f1:
    nb=pickle.load(f1)


pred=nb.predict(t)
st.write(pred)
ze=0
one=0
for i in pred:
    if i==0:
        ze+=1
    else:
        one+=1
        
cnt=[ze,one]       
review= ['Dislike','Like']

labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [15, 30, 45, 10]
explode = (0, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(cnt, labels=review,autopct='%2.2f%%',
        shadow=True, startangle=75)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

img_col[2].pyplot(fig1)
