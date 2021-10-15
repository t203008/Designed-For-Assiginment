import streamlit as st
import pandas as pd
import pycaret

dfa=pd.read_csv("戦力外.csv")
from pycaret.regression import *
reg=setup(dfa,target="DFA")
best_model = compare_models(fold=5)
predict_model(best_model)
st.write(plot_model(best_model))
