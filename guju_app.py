import streamlit as st
import pickle
import joblib

model = joblib.load('guju_model.pkl')
l = []
l.append(st.text_input("Enter text here:"))
if st.button("submit"):
  simple_test = ["મોબાઈલ એપ લોન્ચ: એસટી બસમાં એડવાન્સ કરાવી શકાશે બુકીંગી"]
  pred4 = model.predict(l)
  st.header(pred4[0])