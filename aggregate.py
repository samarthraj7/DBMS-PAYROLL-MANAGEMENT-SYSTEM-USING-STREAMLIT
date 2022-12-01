import streamlit as st
import pandas as pd

from database import aggregate
from database import aggregate_3
from database import aggregate_2



def agg():

    if st.button('Display Bank Count'):
        df=pd.DataFrame(aggregate(),columns=['Bank_Name','Count'])
        st.dataframe(df)
    
    
        
    
    
    
    if st.button('Display Max loan by employee'):
        df=pd.DataFrame(aggregate_3(),columns=['loan'])
        st.dataframe(df)

    if st.button('Display MIN loan by employee'):
        df=pd.DataFrame(aggregate_2(),columns=['loan'])
        st.dataframe(df)