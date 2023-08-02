import csv
import streamlit as st 


def addCSV(a):

    row = {'A': 'Y1', 'B': 'Y2', 'C': 'Y3', "D": a}

    with open('my_file.csv', 'a', newline='') as f:
    
        writer = csv.DictWriter(f, fieldnames=row.keys())
    
        writer.writerow(row)


label = "Your Name"
a = st.text_input(label, value="", max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, args=None, kwargs=None, placeholder=None, disabled=False, label_visibility="visible")

st.button(label, key=None, help=addCSV(a), on_click=None, args=None, kwargs=None, type="secondary", disabled=False, use_container_width=False)


