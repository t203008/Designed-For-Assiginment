import streamlit as st
import pandas as pd
import yellowbrick

from warnings import simplefilter
from sklearn.exceptions import ConvergenceWarning
simplefilter("ignore", category=ConvergenceWarning)
simplefilter(action='ignore', category=FutureWarning)
st.title("戦力外予想")

train=int(st.sidebar.number_input('訓練データ量[%]',0,100,30))
batter=st.sidebar.text_input("打撃データ(NPBのデータをコピペ)",)
pitcher=st.sidebar.text_input("投手データ(NPBのデータをコピペ)",)
p=st.sidebar.number_input("投手での出場試合数",)
c=st.sidebar.number_input("捕手での出場試合数",)
fb=st.sidebar.number_input("一塁手での出場試合数",)
sb=st.sidebar.number_input("二塁手での出場試合数",)
tb=st.sidebar.number_input("三塁手での出場試合数",)
ss=st.sidebar.number_input("遊撃手での出場試合数",)
of=st.sidebar.number_input("外野手での出場試合数",)

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
