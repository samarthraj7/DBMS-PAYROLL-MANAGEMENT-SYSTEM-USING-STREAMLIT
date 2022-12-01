import datetime

import pandas as pd
import streamlit as st
from database import view_all_Employee
from database import view_all_payroll
from database import view_all_data_department
from database import view_all_data_paygrade
from database import view_only_Employee
from database import view_only_payroll
from database import view_only_data_department
from database import view_only_data_paygrade
from database import get_Emp_id
from database import get_paygrade_id
from database import get_department_id
from database import get_payroll
from database import edit_Employee_data
from database import edit_payroll_data
from database import edit_department_data
from database import edit_paygrade_data

def update(table):
    if table=='Employee':
        result = view_all_Employee()
        
        df = pd.DataFrame(result, columns=['Emp_id','fname','lname' ,'dob' ,'phone' ,'email' ,'country' ,'city' ,'pincode','bank_name','department_id'])
        with st.expander("Current Employees"):
            st.dataframe(df)
        list_of_dealers = [i[0] for i in view_only_Employee()]
        selected_dealer = st.selectbox("user to Edit", list_of_dealers)
        selected_result = get_Emp_id(selected_dealer)
        
        if selected_result:
            Emp_id = selected_result[0][0]
            fname = selected_result[0][1]
            lname = selected_result[0][2]
            dob = selected_result[0][3]
            phone = selected_result[0][4]
            email = selected_result[0][5]
            country = selected_result[0][6]
            city = selected_result[0][7]
            pincode = selected_result[0][8]
            bank_name = selected_result[0][9]
            department_id = selected_result[0][10]
            

            col1, col2 = st.columns(2)
            with col1:
                new_Emp_id = st.text_input("Emp_id:",Emp_id)
                new_fname = st.text_input("fname:", fname)
                new_lname = st.text_input("lname:", lname)
                new_dob = st.text_input("dob:", dob)
                new_pincode = st.text_input("pincode:",pincode)
                new_bank_name = st.text_input("bank_name:",bank_name)
            with col2:
                new_phone = st.text_input("phone:",phone)
                new_email = st.text_input("email:",email)
                new_country = st.text_input("city:",country)
                new_city = st.text_input("city:",city)
                
                new_department_id = st.text_input("department_id:",department_id)
            if st.button("Update Employee"):
                edit_Employee_data(new_Emp_id,new_fname,new_lname ,new_dob ,new_phone ,new_email ,new_country ,new_city ,new_pincode,new_bank_name,new_department_id,Emp_id,fname,lname ,dob ,phone ,email ,country ,city ,pincode,bank_name,department_id)
                st.success("Successfully updated:: {} to ::{}".format(Emp_id, new_Emp_id))

        result2 = view_all_Employee()
        df2 = pd.DataFrame(result2, columns=['Emp_id','fname','lname' ,'dob' ,'phone' ,'email' ,'country' ,'city' ,'pincode','bank_name','department_id'])
        with st.expander("Updated data"):
            st.dataframe(df2)



    elif table=='payroll':
        result = view_all_payroll()
        
        df = pd.DataFrame(result, columns=['transaction_id' ,'Emp_id' ,'account_no' ,'bank_name' ,'Emp_net_sal','Emp_sal_yr' ,'Reinbursment_date','loan','grade_id',])
        with st.expander("Current payrolls"):
            st.dataframe(df)
        list_of_dealers = [i[0] for i in view_only_payroll()]
        selected_dealer = st.selectbox("transaction_id to edit", list_of_dealers)
        selected_result = get_payroll(selected_dealer)
        
        if selected_result:
            transaction_id = selected_result[0][0]
            Emp_id = selected_result[0][1]
            account_no = selected_result[0][2]
            bank_name = selected_result[0][3]
            Emp_net_sal = selected_result[0][4]
            Emp_sal_yr= selected_result[0][5]
            loan = selected_result[0][7]
            grade_id = selected_result[0][8]
            Reinbursment_date=selected_result[0][6]

            

            col1, col2 = st.columns(2)
            with col1:
                new_transaction_id = st.text_input("transaction_id:",transaction_id)
                new_Emp_id = st.text_input("Emp_id:", Emp_id)
                new_account_no = st.text_input("account_no:", account_no)
                new_bank_name = st.text_input("bank_name:", bank_name)
                
            with col2:
                new_Emp_net_sal = st.text_input("Emp_net_salary:",Emp_net_sal)
                new_Emp_sal_yr = st.text_input("Emp_sal_yr:",Emp_sal_yr)
                new_loan = st.text_input("loan:",loan)
                new_Reinbursment_date = st.text_input("Reinbursment_date:",Reinbursment_date)
                new_grade_id = st.text_input("grade_id:",grade_id)
                
            if st.button("Update payroll"):
                edit_payroll_data(new_transaction_id,new_Emp_id,new_account_no, new_bank_name,new_Emp_net_sal,new_Emp_sal_yr,new_loan,new_grade_id,new_Reinbursment_date,transaction_id,Emp_id,account_no, bank_name,Emp_net_sal,Emp_sal_yr,loan,grade_id,Reinbursment_date)
                st.success("Successfully updated:: {} to ::{}".format(transaction_id, new_transaction_id))

        result2 = view_all_payroll()
        df2 = pd.DataFrame(result2, columns=['transaction_id' ,'Emp_id' ,'account_no' ,'bank_name' ,'Emp_net_sal','Emp_sal_yr' ,'Reinbursment_date' ,'loan','grade_id'])
        with st.expander("Updated data"):
            st.dataframe(df2)

    elif table=='paygrade':
        result = view_all_data_paygrade()
        
        df = pd.DataFrame(result, columns=['grade_id' , 'grade_name' ,'grade_basic' , 'grade_bonus','department_id'])
        with st.expander("Current paygrades"):
            st.dataframe(df)
        list_of_grade_ids = [i[0] for i in view_only_data_paygrade()]
        selected_grade_id = st.selectbox("paygrade to Edit", list_of_grade_ids)
        selected_result = get_paygrade_id(selected_grade_id)
        
        if selected_result:
            grade_id = selected_result[0][0]
            grade_name = selected_result[0][1]
            department_id = selected_result[0][4]
            grade_basic = selected_result[0][2]
            grade_bonus = selected_result[0][3]
            

            col1, col2 = st.columns(2)
            with col1:
                new_grade_id = st.text_input("grade_id:",grade_id)
                new_grade_name = st.text_input("grade_name:", grade_name)
                new_department_id = st.text_input("department_id:", department_id)
                
            with col2:
                new_grade_basic = st.text_input("grade_basic:",grade_basic)
                new_grade_bonus = st.text_input("grade_bonus:",grade_bonus)
            if st.button("Update paygrade"):
                edit_paygrade_data(new_grade_id,new_grade_name,new_grade_basic,new_grade_bonus,new_department_id,grade_id,grade_name,grade_basic,grade_bonus,department_id)
                st.success("Successfully updated:: {} to ::{}".format(grade_id, new_grade_id))

        result2 = view_all_data_paygrade()
        df2 = pd.DataFrame(result2, columns=['grade_id' , 'grade_name' ,'grade_basic' , 'grade_bonus','department_id'])
        with st.expander("Updated data"):
            st.dataframe(df2)



    elif table=='department':
        result = view_all_data_department()
        
        df = pd.DataFrame(result, columns=['department_id', 'department_name'])
        with st.expander("Current department"):
            st.dataframe(df)
        list_of_dealers = [i[0] for i in view_only_data_department()]
        selected_dealer = st.selectbox("department to Edit", list_of_dealers)
        selected_result = get_department_id(selected_dealer)
        
        if selected_result:
            department_id = selected_result[0][0]
            department_name = selected_result[0][1]
            
            
            

            col1, col2 = st.columns(2)
            with col1:
                new_department_id = st.text_input("department_id:",department_id)
                
            with col2:
                new_department_name = st.text_input("department_name:",department_name)
                
            if st.button("Update department_details"):
                edit_department_data(new_department_id, new_department_name,department_id,department_name)
                st.success("Successfully updated:: {} to ::{}".format(department_id, new_department_id))

        result2 = view_all_data_department()
        df2 = pd.DataFrame(result2, columns=['department_id', 'department_name'])
        with st.expander("Updated data"):
            st.dataframe(df2)



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
                
    
    
    
    
    
    
    
    

    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    



    
    
    
    
    
    
    
    
    
    
    
    
    
    

    

    
    
    
    
                
    
    

                
    
    
    

    
    
    
    

