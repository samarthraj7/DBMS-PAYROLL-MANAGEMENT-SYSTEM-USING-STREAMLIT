import streamlit as st
import pandas as pd
from database import joining_2
from database import joining
from database import joining_3


def join():

    if st.button('Display Join On payroll and Employee'):
        df=pd.DataFrame(joining(),columns=['Emp_id','bank_name',"transaction_id","city","loan","fname","Emp_Net_sal"])
        st.dataframe(df)
    if st.button('Display Join On paygrade and department'):
        df=pd.DataFrame(joining_2(),columns=['department_id','department_name','grade_id','grade_name','grade_bonus'])
        st.dataframe(df)

    if st.button('Display Join On Employee and department'):
        df=pd.DataFrame(joining_3(),columns=['department_id', 'Emp_id', 'fname','lname'])
        st.dataframe(df)
    
    
    