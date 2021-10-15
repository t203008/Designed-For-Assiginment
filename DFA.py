import streamlit as st
import pandas as pd
import yellowbrick
from warnings import simplefilter
from sklearn.exceptions import ConvergenceWarning
simplefilter("ignore", category=ConvergenceWarning)
simplefilter(action='ignore', category=FutureWarning)

dfa=pd.read_csv("戦力外.csv")
X=dfa.drop("DFA",axis=1)
st.write(X)
