import streamlit as st
import pandas as pd
import pycaret

dfa=pd.read_csv("戦力外.csv")

reg=setup(dfa,target="DFA")
st.write(reg)
