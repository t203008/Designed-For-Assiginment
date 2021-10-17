import streamlit as st
import pandas as pd
import yellowbrick

from warnings import simplefilter
from sklearn.exceptions import ConvergenceWarning
simplefilter("ignore", category=ConvergenceWarning)
simplefilter(action='ignore', category=FutureWarning)

st.title("戦力外予想")
train=int(st.sidebar.number_input('訓練データ量[%]',0,100,30))

dfa=pd.read_csv("戦力外.csv")
dfa=dfa.drop(columns=dfa.columns[[0,67]],axis=1)
dfa = pd.get_dummies(dfa, drop_first=True) 
dfa=dfa.fillna(0)
dfa=dfa.astype(float)

y=dfa["DFA"]
X=dfa.drop("DFA",axis=1)
st.write(X)

from sklearn.model_selection import train_test_split 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=train/100)

from sklearn.linear_model import LogisticRegression
logreg=LogisticRegression()
logreg.fit(X_train,y_train)
y_pred = logreg.predict(X_test)

from sklearn import metrics
st.write(metrics.accuracy_score(y_test,y_pred))

batter=st.sidebar.text_input("打撃データ(NPBのデータの試合から出塁率までをコピペ)",)
pitcher=st.sidebar.text_input("投手データ(NPBのデータの登板から防御率をコピペ)",)
pf=st.sidebar.text_input("投手での守備データ(NPBのデータの試合から併殺までをコピペ)",)
cf=st.sidebar.text_input("捕手での守備データ(NPBのデータの試合から捕逸までをコピペ)",)
fbf=st.sidebar.text_input("一塁手での守備データ(NPBのデータの試合から併殺までをコピペ)",)
sbf=st.sidebar.text_input("二塁手での守備データ(NPBのデータの試合から併殺までをコピペ)",)
tbf=st.sidebar.text_input("三塁手での守備データ(NPBのデータの試合から併殺までをコピペ)",)
ssf=st.sidebar.text_input("遊撃手での守備データ(NPBのデータの試合から併殺までをコピペ)",)
off=st.sidebar.text_input("外野での守備データ(NPBのデータの試合から併殺までをコピペ)",)

b=batter.split()
b=[float(n) for n in b]
st.write(b)

p=pitcher.split()
p=[float(n) for n in p]
if len(p)==0:
  p=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
st.write(p)

pf=pf.split()
if len(pf)==0:
  pf=[0,0,0,0,0,0]
else:
  pf.append(0)
pf=[float(n) for n in pf]
  
cf=cf.split()
if len(cf)==0:
  cf=[0,0,0,0,0,0]
cf=[float(n) for n in cf]
  
fbf=fbf.split()
fbf.append(0)
if len(fbf)==0:
  fbf=[0,0,0,0,0,0]
else:
  fbf.append(0)
fbf=[float(n) for n in fbf]
  
sbf=sbf.split()
sbf.append(0)
if len(sbf)==0:
  sbf=[0,0,0,0,0,0]
else:
  sbf.append(0)
sbf=[float(n) for n in sbf]

tbf=tbf.split()
tbf.append(0)
if len(tbf)==0:
  tbf=[0,0,0,0,0,0]
else:
  tbf.append(0)
tbf=[float(n) for n in tbf]

ssf=ssf.split()
ssf.append(0)
if len(ssf)==0:
  ssf=[0,0,0,0,0,0]
else:
  ssf.append(0)
ssf=[float(n) for n in ssf]

off=off.split()
off.append(0)
if len(off)==0:
  off=[0,0,0,0,0,0]
else:
  off.append(0)
off=[float(n) for n in off]

a=[pf[0]+cf[0]+fbf[0]+sbf[0]+tbf[0]+ssf[0]+off[0],pf[1]+cf[1]+fbf[1]+sbf[1]+tbf[1]+ssf[1]+off[1],pf[2]]
st.write(a)
fielding=[pf[0]+cf[0]+fbf[0]+sbf[0]+tbf[0]+ssf[0]+off[0],pf[1]+cf[1]+fbf[1]+sbf[1]+tbf[1]+ssf[1]+off[1],pf[2]+cf[2]+fbf[2]+sbf[2]+tbf[2]+ssf[2]+off[2],pf[3]+cf[3]+fbf[3]+sbf[3]+tbf[3]+ssf[3]+off[3],pf[4]+cf[4]+fbf[4]+sbf[4]+tbf[4]+ssf[4]+off[4],pf[5]+cf[5]+fbf[5]+sbf[5]+tbf[5]+ssf[5]+off[5]]
st.write(fielding)
