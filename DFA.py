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

from sklearn.linear_model import LinearRegression
reg = LinearRegression()
reg.fit(X, y)
yhat = reg.predict(X)
