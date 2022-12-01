import pandas as pd
import streamlit as st
import plotly.express as px
from database import view_all_Employee
from database import view_all_payroll
from database import view_all_data_department
from database import view_all_data_paygrade

def read(table):
    if table=='Employee':
        result = view_all_Employee()
        
        df = pd.DataFrame(result, columns=['Emp_id','fname','lname' ,'dob' ,'phone' ,'email' ,'country' ,'city' ,'pincode','bank_name','department_id'])
        with st.expander("View all Employees"):
            st.dataframe(df)
        with st.expander("user city"):
            task_df = df['city'].value_counts().to_frame()
            task_df = task_df.reset_index()
            st.dataframe(task_df)
            p1 = px.pie(task_df, names='index', values='city')
            st.plotly_chart(p1)


    elif table=='payroll':
        result = view_all_payroll()
        
        df = pd.DataFrame(result, columns=['transaction_id' ,'Emp_id' ,'account_no' ,'bank_name' ,'Emp_net_sal','Emp_sal_yr' ,'Reinbursment_date' ,'loan','grade_id'])
        with st.expander("View all payrolls"):
            st.dataframe(df)
        with st.expander("user Bank_name"):
            task_df = df['bank_name'].value_counts().to_frame()
            task_df = task_df.reset_index()
            st.dataframe(task_df)
            p1 = px.pie(task_df, names='index', values='bank_name')
            st.plotly_chart(p1)

    elif table=='paygrade':
        result = view_all_data_paygrade()
        
        df = pd.DataFrame(result, columns=['grade_id' , 'grade_name' ,'grade_basic' , 'grade_bonus','department_id'])
        with st.expander("View all paygrades"):
            st.dataframe(df)
        with st.expander("user pays"):
            task_df = df['grade_id'].value_counts().to_frame()
            task_df = task_df.reset_index()
            st.dataframe(task_df)
            p1 = px.pie(task_df, values='grade_id')
            st.plotly_chart(p1)


    elif table=='department':
        result = view_all_data_department()
        
        df = pd.DataFrame(result, columns=['department_id', 'department_name'])
        with st.expander("View all departments"):
            st.dataframe(df)


    
    
    
    
    
    
    
    
    
    
    
    


    
    
    
    
    
    
        


    
    
    
    
    
    
        

