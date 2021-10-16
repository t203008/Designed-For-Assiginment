import streamlit as st
import pandas as pd
import yellowbrick

from warnings import simplefilter
from sklearn.exceptions import ConvergenceWarning
simplefilter("ignore", category=ConvergenceWarning)
simplefilter(action='ignore', category=FutureWarning)

dfa=pd.read_csv("戦力外.csv")

dfa = pd.get_dummies(dfa, drop_first=True) 

y=dfa["DFA"]
X=dfa.drop(["DFA","名前"],axis=1)

from sklearn.linear_model import LogisticRegression
logreg =  LogisticRegression()
logreg.fit(X, y)
