import streamlit as st
import pandas as pd
from database import info
from database import infop


def info_1():
    if st.button('Display the information which was implemented using curser'):
        df=pd.DataFrame(info(),columns=['First_name','Last_name','Email'])
        st.dataframe(df)


    if st.button('Display the tax table and final salary of all the employees using curser'):
        df=pd.DataFrame(infop(),columns=['First_name','tax','loan','Emp_net_sal','Gross_sal'])
        st.dataframe(df)