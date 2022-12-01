import pickle 
from pathlib import Path
import streamlit_authenticator as stauth
import streamlit as st
import mysql.connector
from create import create
from database import create_table
from delete import delete
from read import read
from update import update
from function import loan_1
from join import join
from aggregate import agg
from union import uni
from queries import execute_query
from inter import inter
from procedure import info_1

mydb = mysql.connector.connect(
    host="localhost",
    user="root"
)
c = mydb.cursor()


c.execute("use pes1ug20cs370_fp")
names=["samarth","sanjay","sanmat","sanath","shamith","sathwick","manu","sonu","ronu"]
usernames = ["samarth","sanjay","sanmat","sanath","shamith","sathwick","manu","sonu","ronu"]

file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)

authenticator = stauth.Authenticate(names,usernames, hashed_passwords, "sales_dashboard", "1234", cookie_expiry_days=0)

names,authentication_status, username = authenticator.login("Login", "main")


if authentication_status == False :
        st.error("Username/password is incorrect")

if authentication_status == None :
        st.warning("Please enter your username and password")

if authentication_status :
    st.title("PAYROLL MANAGEMENT SYSTEM")


    def main():
        authenticator.logout("Logout", "sidebar")
        menu = ["Add", "View", "Edit", "Remove",
                "Function", "Join", "Aggregate", "Query", "UNION","INTERSECTION","procedure"]
        table_names = ["Employee", "payroll", "paygrade", "department"]

        table = st.sidebar.selectbox("table", table_names)
        choice = st.sidebar.selectbox("action", menu)
        create_table(table)
        if choice == "Add":
            if table == 'Employee':
                st.subheader("Enter Employee Details:")
                create(table)
            elif table == 'payroll':
                st.subheader("Enter payroll Details:")
                create(table)
            elif table == 'paygrade':
                st.subheader("Enter paygrade Details:")
                create(table)
            elif table == 'department':
                st.subheader("Enter department Details:")
                create(table)
        
        if choice == "View":
            if table == 'Employee':
                st.subheader("view Employee Details:")
                read(table)
            elif table == 'payroll':
                st.subheader("view payroll Details:")
                read(table)
            elif table == 'paygrade':
                st.subheader("view paygrade Details:")
                read(table)
            elif table == 'department':
                st.subheader("view department Details:")
                read(table)
        
        if choice == "Remove":
            if table == 'Employee':
                st.subheader("Delete enetered Employee Details:")
                delete(table)
            elif table == 'payroll':
                st.subheader("Delete entered payroll Details:")
                delete(table)
            elif table == 'paygrade':
                st.subheader("Delete paygrade:")
                delete(table)
            elif table == 'department':
                st.subheader("Delete entered department Details:")
                delete(table)
            
            
        if choice == "Edit":
            if table == 'Employee':
                st.subheader("Update entered Employee Details:")
                update(table)
            elif table == 'payroll':
                st.subheader("Update entered payroll Details:")
                update(table)
            elif table == 'paygrade':
                st.subheader("Update entered paygrade Details:")
                update(table)
            elif table == 'department':
                st.subheader("Update entered department Details:")
                update(table)
            
            
        if choice == 'Function':
            st.subheader("CAN YOU APPLY FOR LOAN?")
            loan_1()

        if choice == 'Join':
            st.subheader("join:")
            join()

        if choice == 'Aggregate':
            st.subheader("Aggregate:")
            agg()

        if choice == 'Query':
            st.subheader("Enter QUERY:")
            execute_query()
        
        if choice == 'UNION':
            st.subheader("UNION:")
            uni()
        

        if choice == 'INTERSECTION':
            st.subheader("Intersection:")
            inter()
        
        if choice == 'procedure':
            st.subheader("PROCEDURE:")
            info_1()

        
        
        


    if __name__ == '__main__':
        main()
