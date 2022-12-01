import streamlit as st
from database import add_data_Employee
from database import add_data_payroll
from database import add_data_department
from database import add_data_paygrade




def create(table):
    if table=='Employee':
        col1, col2 = st.columns(2)
        with col1:
            Emp_id = st.text_input("Emp_id:")
            fname = st.text_input("fname:")
            lname =  st.text_input("lname:")
            dob =  st.date_input("dob:")
            phone =  st.text_input("phone:")

        with col2:
            department_id = st.text_input("department_id")
            email = st.text_input("email:")
            country = st.text_input("country:")
            city = st.text_input("city:")
            pincode= st.text_input("pincode:")
            bank_name = st.text_input("bank_name:")


        if st.button("Add data"):
            add_data_Employee(Emp_id,fname,lname ,dob ,phone ,email ,country ,city ,pincode,bank_name,department_id)
            st.success("Successfully booked : {}".format(Emp_id))

    elif table=='payroll':
        col1, col2 = st.columns(2)
        with col1:
            transaction_id = st.text_input("transaction_id:")
            Emp_id = st.text_input("Emp_id:")
            account_no =  st.text_input("account_no:")
            bank_name = st.text_input("bank_name:")

        with col2:
            Emp_net_sal = st.text_input("Emp_net_sal")
            Emp_sal_yr= st.text_input("Emp_sal_yr:")
            Reinbursment_date = st.date_input("Reinbursment_date:")
            loan = st.text_input("loan:")
            grade_id = st.text_input("grade_id:")
        if st.button("Add data"):
            add_data_payroll(transaction_id,Emp_id,account_no, bank_name,Emp_net_sal,Emp_sal_yr,loan,grade_id,Reinbursment_date)
            st.success("Successfully added : {}".format(transaction_id))

    elif table == 'paygrade':
        col1, col2 = st.columns(2)
        with col1:
            grade_id = st.text_input("grade_id:")
            grade_name = st.text_input("grade_name:")
            department_id = st.text_input("department_id:")
            
        with col2:
            grade_basic = st.text_input("grade_basic:")
            grade_bonus = st.text_input("grade_bonus:")
            

        if st.button("Add data"):
            add_data_paygrade(grade_id,grade_name,grade_bonus,grade_basic,department_id)
            st.success("Successfully added : {}".format(grade_id))


    elif table == 'department':
        col1, col2 = st.columns(2)
        with col1:
            department_id = st.text_input("department_id:")
            
            
            
            
        with col2:
            department_name = st.text_input("department_name:")
            
            

        if st.button("Add data"):
            add_data_department(department_id, department_name)
            st.success("Successfully added : {}".format(department_id))


    
    
    
    
    
    
    
    
    
    
    

    
    
    


    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    

    
    
    
    
    
    

    
    
    


    
