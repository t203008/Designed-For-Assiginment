import streamlit as st
import pandas as pd
import yellowbrick

from warnings import simplefilter
from sklearn.exceptions import ConvergenceWarning
simplefilter("ignore", category=ConvergenceWarning)
simplefilter(action='ignore', category=FutureWarning)
st.title("戦力外予想")

train=int(st.sidebar.number_input('訓練データ量',0,1,0))

dfa=pd.read_csv("戦力外.csv")
dfa = pd.get_dummies(dfa, drop_first=True) 
dfa=dfa.fillna(0)
dfa=dfa.astype(float)

y=dfa["DFA"]
X=dfa.drop("DFA",axis=1)

from sklearn.model_selection import train_test_split 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=train)

logreg=LogisticRegression()
logreg.fit(X_train,y_train)
y_pred = logreg.predict(X_test)

from sklearn import metrics
st.write(metrics.accuracy_score(y_test,y_pred))
