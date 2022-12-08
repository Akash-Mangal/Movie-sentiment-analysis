import pickle
import pandas as pd
import re

import numpy as np



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

n=int(input("Enter number of comments "))
inp=[]
for i in range(n):
    inp.append(input("Enter statements.\n"))

f=[]
for i in inp:
    s=clean(i)
    f.append(s)

with open("Akash Agarwal_18 AiMl+DS_ Movie sentiment analysis/cv1.pkl",'rb') as f1:
    cv1=pickle.load(f1)
t=cv1.transform(f).toarray()

with open("Akash Agarwal_18 AiMl+DS_ Movie sentiment analysis/nb_model.pkl",'rb') as f1:
    nb=pickle.load(f1)

pred=nb.predict(t)
print(pred)
ze=0
one=0
for i in pred:
    if i==0:
        ze+=1
    else:
        one+=1
        
cnt=[ze,one]       
review= ['Bad','Good']
plt.bar(review,cnt,width=.2)

plt.show()
