import streamlit as st
import pandas as pd
from database import intersection_1

def inter():

    if st.button('Display intersection On payroll and Employee'):
        df=pd.DataFrame(intersection_1(),columns=['Emp_id'])
        st.dataframe(df)