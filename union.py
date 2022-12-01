import streamlit as st
import pandas as pd
from database import union_1

def uni():

    if st.button('Display union On payroll and Employee'):
        df=pd.DataFrame(union_1(),columns=['Emp_id'])
        st.dataframe(df)