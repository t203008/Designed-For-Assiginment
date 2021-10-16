import streamlit as st
import pandas as pd
import yellowbrick
from warnings import simplefilter
from sklearn.exceptions import ConvergenceWarning
simplefilter("ignore", category=ConvergenceWarning)
simplefilter(action='ignore', category=FutureWarning)

dfa=pd.read_csv("戦力外.csv")
<<<<<<< Updated upstream
st.write(dfa.head())
=======
from pycaret.regression import *
reg=setup(dfa,target="DFA")
st.write(reg)

>>>>>>> Stashed changes
