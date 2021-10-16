import streamlit as st
import pandas as pd
import yellowbrick

from warnings import simplefilter
from sklearn.exceptions import ConvergenceWarning
simplefilter("ignore", category=ConvergenceWarning)
simplefilter(action='ignore', category=FutureWarning)

dfa=pd.read_csv("戦力外.csv")
dfa = pd.get_dummies(dfa, drop_first=True) 
dfa=dfa.fillna(0)
dfa=dfa.astype(float)

y=dfa["DFA"]
X=dfa.drop(["DFA","名前"],axis=1)

from sklearn.model_selection import train_test_split 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

from sklearn.linear_model import LogisticRegression
logreg=LogisticRegression()
logreg.fit(X_train,y_train)
y_pred = logreg.predict(X_test)

from sklearn import metrics
st.write(metrics.accuracy_score(y_test,y_pred))

dfa=pd.read_csv("戦力外.csv")
dfa = pd.get_dummies(dfa, drop_first=True) 
dfa=dfa.fillna(0)
dfa=dfa.astype(float)
y=dfa["DFA"]
X=dfa.drop(["DFA","名前"],axis=1)

from yellowbrick.classifier import ConfusionMatrix
logreg=LogisticRegression()
logreg.fit(X,y)
cm = ConfusionMatrix(logreg, classes=["not dfa", "is dfa"])
cm.fit(X,y)
cm.score(X,y)
st.write(cm)

from yellowbrick.classifier import ROCAUC

visualizer = ROCAUC(logreg, size=(600,400))

visualizer.fit(X, y)
visualizer.score(X, y)
st.write(visualizer)
