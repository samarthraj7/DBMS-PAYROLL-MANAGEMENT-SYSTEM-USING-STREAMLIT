import pandas as pd
import streamlit as st
from database import view_only_Employee
from database import view_only_payroll
from database import view_only_data_department
from database import view_only_data_paygrade
from database import view_all_Employee
from database import view_all_payroll
from database import view_all_data_paygrade
from database import view_all_data_department
from database import delete_Employee
from database import delete_payroll
from database import delete_paygrade
from database import delete_department

def delete(table):
    if table=='Employee':
        result = view_all_Employee()
        df = pd.DataFrame(result, columns=['Emp_id','fname','lname' ,'dob' ,'phone' ,'email' ,'country' ,'city' ,'pincode','bank_name','department_id'])
        with st.expander("Current data"):
            st.dataframe(df)

        list_of_user = [i[0] for i in view_only_Employee()]
        selected_user = st.selectbox("Task to Delete", list_of_user)
        st.warning("Do you want to delete ::{}".format(selected_user))
        if st.button("Delete user"):
            delete_Employee(selected_user)
            st.success("Employee has been deleted successfully")
        new_result = view_all_Employee()
        df2 = pd.DataFrame(new_result, columns=['Emp_id','fname','lname' ,'dob' ,'phone' ,'email' ,'country' ,'city' ,'pincode','bank_name','department_id'])
        with st.expander("Updated data"):
            st.dataframe(df2)

    elif table=='payroll':
        result = view_all_payroll()
        df = pd.DataFrame(result, columns=['transaction_id' ,'Emp_id' ,'account_no' ,'bank_name' ,'Emp_net_sal','Emp_sal_yr' ,'loan','grade_id','Reinbursment_date'])
        with st.expander("Current data"):
            st.dataframe(df)

        list_of_user = [i[0] for i in view_only_payroll()]
        selected_user = st.selectbox("Task to Delete", list_of_user)
        st.warning("Do you want to delete ::{}".format(selected_user))
        if st.button("Delete payroll"):
            delete_payroll(selected_user)
            st.success("payroll has been deleted successfully")
        new_result = view_all_payroll()
        df2 = pd.DataFrame(new_result, columns=['transaction_id' ,'Emp_id' ,'account_no' ,'bank_name' ,'Emp_net_sal','Emp_sal_yr' ,'loan','grade_id','Reinbursment_date'])
        with st.expander("Updated data"):
            st.dataframe(df2)

    elif table=='paygrade':
        result = view_all_data_paygrade()
        df = pd.DataFrame(result, columns=['grade_id' , 'grade_name' ,'grade_basic' , 'grade_bonus','department_id'])
        with st.expander("Current data"):
            st.dataframe(df)

        list_of_user = [i[0] for i in view_only_data_paygrade()]
        selected_user = st.selectbox("Task to Delete", list_of_user)
        st.warning("Do you want to delete ::{}".format(selected_user))
        if st.button("Delete paygrades"):
            delete_paygrade(selected_user)
            st.success("paygrade has been deleted successfully")
        new_result = view_all_data_paygrade()
        df2 = pd.DataFrame(new_result, columns=['grade_id' , 'grade_name' ,'grade_basic' , 'grade_bonus','department_id'])
        with st.expander("Updated data"):
            st.dataframe(df2)

    elif table=='department':
        result = view_all_data_department()
        df = pd.DataFrame(result, columns=['department_id', 'department_name'])
        with st.expander("Current data"):
            st.dataframe(df)

        list_of_user = [i[0] for i in view_only_data_department()]
        selected_user = st.selectbox("Task to Delete", list_of_user)
        st.warning("Do you want to delete ::{}".format(selected_user))
        if st.button("Delete departments"):
            delete_department(selected_user)
            st.success("department has been deleted successfully")
        new_result = view_all_data_department()
        df2 = pd.DataFrame(new_result, columns=['department_id', 'department_name'])
        with st.expander("Updated data"):
            st.dataframe(df2)

    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    

    
    
    
    
    

    
    
    
    
    
    
    
    
    
    

    




