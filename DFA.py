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
dfa = pd.get_dummies(dfa, drop_first=True) 
dfa=dfa.fillna(0)
dfa=dfa.astype(float)

y=dfa["DFA"]
X=dfa.drop("DFA",axis=1)

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
st.write(p)
