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

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
from sklearn import tree
tree_class = tree.DecisionTreeClassifier()
tree_class.fit(X_train, y_train)
yhat = tree_class.predict(X_test)
st.write(metrics.accuracy_score(y_test, yhat))

dfa=pd.read_csv("戦力外.csv")
dfa = pd.get_dummies(dfa, drop_first=True) 
dfa=dfa.fillna(0)
dfa=dfa.astype(float)

y=dfa["DFA"]
X=dfa.drop(["DFA","名前"],axis=1)

from sklearn.ensemble import RandomForestRegressor
rf = RandomForestRegressor()
rf.fit(X, y)

from sklearn.inspection import permutation_importance
result = permutation_importance(rf, X, y)
st.write(result.importances_mean)

#from sklearn.linear_model import LogisticRegression
#logreg =  LogisticRegression()
#logreg.fit(X, y)

#st.write(dfa)
