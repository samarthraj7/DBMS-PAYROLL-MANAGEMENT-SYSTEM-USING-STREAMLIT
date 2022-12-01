# DBMS-PAYROLL-MANAGEMENT-SYSTEM-USING-STREAMLIT

Database Management System project on Payroll Management using Streamlit as the front end
Modules needed:
1} streamlit
2) streamlit-authenticator
3) mysql.connector-python 
4) pickle
5) pathlib
6) XAMPP needs to installed prior to it and mysql.

If XAMPP crashes 
Steps to be done:
1) GO to Xampp folder in C drive Xampp->mysql->data , Copy all the files in it.
2) create new folder DataOld and paste in it,and delete everything in Data folder
3) go to backup folder , Copy everything and paste it in data
4) go to dataold created in step2 and copy the databases you need and ibdata1 and test folder and replace the files in Data folder and Xampp should work.

ER diagram is uploaded as draw.io file with Relational Schema.
hasedpw.pkl file is the one which stores the password for login data. To create that you need to run the generate.py file.

Running of the files
after installing the modules go the folder and open the cmd and run
====> streamlit run app.py
to check the backend of the database you need to check in mysql maria DB in cmd or PHPMYADMIN localhost server

Images of it are present in the project report (PES1UG20CS370.pdf)
