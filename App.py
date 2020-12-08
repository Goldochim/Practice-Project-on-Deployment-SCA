# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 22:46:48 2020

@author: DELL
"""
import streamlit as st
import pickle
import sklearn

pickle_in=open('clfTitanic.pkl', 'rb')
clf=pickle.load(pickle_in)

def welcome():
    return "Welcome All"

def Titanic_Prediction(Sex, Age, PClass,Siblings_Spouses_Aboard, Parents_Children_Aboard, Fare):
    prediction=clf.predict(['Sex', 'Age', 'PClass,Siblings/Spouses Aboard', 'Parents/Children Aboard', 'Fare'])
    print(prediction)
    return 'The prediction value is '+str(prediction)

def main():
    st.title("Titanic prediction App")
    html_temp="""
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Titanic App</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    Sex=st.text_input("Sex", "Type here")
    Age=st.text_input("Age", "Type here")
    PClass=st.text_input("PClass", "Type here")
    Siblings_Spouses_Aboard=st.text_input("Siblings/Spouses Aboard", "Type here")
    Parents_Children_Aboard=st.text_input("Parents/Children Aboard", "Type here")
    Fare=st.text_input("Fare", "Type here")
    result=""
    if st.button("Predict"):
        result=Titanic_Prediction(Sex, Age, PClass,Siblings_Spouses_Aboard, Parents_Children_Aboard, Fare)
    st.success('The Titanic Survival Prediction is {}'.format(result))
    if st.button("Prediction Note"):
        st.text("0-passenger live, 1=Passenger Die")
        
if __name__=='__main__':
    main()
