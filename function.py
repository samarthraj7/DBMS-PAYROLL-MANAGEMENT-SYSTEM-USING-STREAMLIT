import streamlit as st
import pandas as pd
from database import loan



def loan_1():
    
    x = st.text_input("Enter Balance in your account:")
    if st.button('Validate'):
        
        
        
        if int(x) > 10000:
            st.success("yes")
        else:
            st.success("no")

        
        
        
        
