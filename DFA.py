import streamlit as st
import pandas as pd
import yellowbrick

from warnings import simplefilter
from sklearn.exceptions import ConvergenceWarning
simplefilter("ignore", category=ConvergenceWarning)
simplefilter(action='ignore', category=FutureWarning)

dfa=pd.read_csv("戦力外.csv")
y=dfa["DFA"]
X =dfa.drop("DFA",axis=1)

from sklearn.linear_model import LogisticRegression
logreg =  LogisticRegression()
logreg.fit(X,y)

from yellowbrick.classifier import ConfusionMatrix

cm = ConfusionMatrix(logreg, classes=["not dfa", "is dfa"])

cm.fit(X, y)
cm.score(X, y)
st.write(cm.show();)
