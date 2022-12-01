
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    database="pes1ug20cs370_fP"
)
c = mydb.cursor()

def create_table(table):
    if table=='Employee':
        c.execute('CREATE TABLE IF NOT EXISTS Employee(Emp_id TEXT,fname TEXT,lname TEXT,dob TEXT,phone TEXT,email TEXT,country TEXT,city TEXT,pincode TEXT,bank_name TEXT,department_id TEXT)')
    elif table=='payroll':
        c.execute('CREATE TABLE IF NOT EXISTS payroll(transaction_id TEXT ,Emp_id TEXT,account_no TEXT, bank_name TEXT,Emp_net_sal TEXT,Emp_sal_yr TEXT,Reinbursment_date TEXT,loan TEXT,grade_id TEXT)')
    elif table=='paygrade':
        c.execute('CREATE TABLE IF NOT EXISTS paygrade(grade_id TEXT, grade_name TEXT,grade_basic TEXT, grade_bonus TEXT,department_id TEXT)')
    elif table=='department':
        c.execute('CREATE TABLE IF NOT EXISTS department(department_id TEXT,department_name TEXT)')
    
def add_data_Employee(Emp_id,fname,lname ,dob ,phone ,email ,country ,city ,pincode,bank_name,department_id):
        c.execute('INSERT INTO Employee(Emp_id,fname,lname ,dob ,phone ,email ,country ,city ,pincode,bank_name,department_id) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                  (Emp_id,fname,lname ,dob ,phone ,email ,country ,city ,pincode,bank_name,department_id))
        mydb.commit()

def add_data_payroll(transaction_id ,Emp_id ,account_no , bank_name ,Emp_net_sal,Emp_sal_yr ,loan,grade_id,Reinbursment_date):
        c.execute('INSERT INTO payroll(transaction_id ,Emp_id ,account_no , bank_name ,Emp_net_sal,Emp_sal_yr ,loan,grade_id,Reinbursment_date) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                  (transaction_id ,Emp_id ,account_no , bank_name ,Emp_net_sal,Emp_sal_yr ,loan,grade_id,Reinbursment_date))
        mydb.commit()

def add_data_paygrade(grade_id , grade_name ,grade_basic , grade_bonus ,department_id):
        c.execute('INSERT INTO paygrade(grade_id , grade_name ,grade_basic , grade_bonus , department_id ) VALUES (%s,%s,%s,%s,%s)',
                  (grade_id , grade_name ,grade_basic , grade_bonus,department_id))
        mydb.commit()


def add_data_department(department_id, department_name):
        c.execute('INSERT INTO department(department_id, department_name) VALUES (%s,%s)',
                  (department_id, department_name))
        mydb.commit()


def view_all_Employee():
    c.execute('SELECT * FROM Employee')
    data = c.fetchall()
    return data
def view_all_payroll():
    c.execute('SELECT * FROM payroll')
    data = c.fetchall()
    return data
def view_all_data_paygrade():
    c.execute('SELECT * FROM paygrade')
    data = c.fetchall()
    return data
def view_all_data_department():
    c.execute('SELECT * FROM department')
    data = c.fetchall()
    return data

def view_only_Employee():
    c.execute('SELECT Emp_id FROM Employee')
    data = c.fetchall()
    return data
def view_only_payroll():
    c.execute('SELECT transaction_id FROM payroll')
    data = c.fetchall()
    return data
def view_only_data_paygrade():
    c.execute('SELECT grade_id FROM paygrade')
    data = c.fetchall()
    return data
def view_only_data_department():
    c.execute('SELECT department_id FROM department')
    data = c.fetchall()
    return data


def get_Emp_id(Emp_id):
    c.execute('SELECT * FROM Employee WHERE Emp_id="{}"'.format(Emp_id))
    data = c.fetchall()
    return data
def get_payroll(transaction_id):
    c.execute('SELECT * FROM payroll WHERE transaction_id="{}"'.format(transaction_id))
    data = c.fetchall()
    return data

def get_paygrade_id(grade_id):
    c.execute('SELECT * FROM paygrade WHERE grade_id="{}"'.format(grade_id))
    data = c.fetchall()
    return data

def get_department_id(department_id):
    c.execute('SELECT * FROM department WHERE department_id="{}"'.format(department_id))
    data = c.fetchall()
    return data


def edit_Employee_data(new_Emp_id,new_fname,new_lname ,new_dob ,new_phone ,new_email ,new_country ,new_city ,new_pincode,new_bank_name,new_department_id,Emp_id,fname,lname ,dob ,phone ,email ,country ,city ,pincode,bank_name,department_id):
    c.execute("UPDATE Employee SET Emp_id=%s,fname=%s, lname=%s, dob=%s, phone=%s,email=%s,country=%s,city=%s,pincode=%s,bank_name=%s,department_id=%s WHERE "
              "Emp_id=%s and fname=%s and lname=%s and dob=%s and phone=%s and email=%s and country=%s and city=%s and pincode=%s and bank_name=%s and department_id=%s",(new_Emp_id,new_fname,new_lname ,new_dob ,new_phone ,new_email ,new_country ,new_city ,new_pincode,new_bank_name,new_department_id,Emp_id,fname,lname ,dob ,phone ,email ,country ,city ,pincode,bank_name,department_id))
    mydb.commit()
    data = c.fetchall()
    return data

def edit_payroll_data(new_transaction_id ,new_Emp_id ,new_account_no , new_bank_name ,new_Emp_net_sal,new_Emp_sal_yr ,new_loan,new_grade_id,new_Reinbursment_date,transaction_id,Emp_id,account_no, bank_name,Emp_net_sal,Emp_sal_yr,loan,grade_id,Reinbursment_date):
    c.execute("UPDATE payroll SET transaction_id=%s ,Emp_id=%s ,account_no=%s , bank_name=%s ,Emp_net_sal=%s,Emp_sal_yr=%s ,loan=%s ,grade_id=%s,Reinbursment_date=%s WHERE "
              "transaction_id=%s and Emp_id=%s and account_no=%s and bank_name=%s and Emp_net_sal=%s and Emp_sal_yr=%s and loan=%s and grade_id=%s and Reinbursment_date=%s", (new_transaction_id ,new_Emp_id ,new_account_no , new_bank_name ,new_Emp_net_sal,new_Emp_sal_yr ,new_loan,new_grade_id,new_Reinbursment_date,transaction_id,Emp_id,account_no, bank_name,Emp_net_sal,Emp_sal_yr,loan,grade_id,Reinbursment_date))
    mydb.commit()
    data = c.fetchall()
    return data

def edit_paygrade_data(new_grade_id , new_grade_name ,new_grade_basic , new_grade_bonus,new_department_id,grade_id,grade_name,grade_basic,grade_bonus,department_id):
    c.execute("UPDATE paygrade SET grade_id=%s , grade_name=%s ,grade_basic=%s , grade_bonus=%s,department_id=%s WHERE "
              "grade_id=%s and grade_name=%s and grade_basic=%s and grade_bonus=%s and department_id=%s ", (new_grade_id , new_grade_name ,new_grade_basic , new_grade_bonus,new_department_id,grade_id,grade_name,grade_basic,grade_bonus,department_id))
    mydb.commit()
    data = c.fetchall()
    return data


def edit_department_data(new_department_id, new_department_name,department_id,department_name):
    c.execute("UPDATE department SET department_id=%s, department_name=%s WHERE "
              "department_id=%s and department_name=%s ", (new_department_id, new_department_name,department_id,department_name))
    mydb.commit()
    data = c.fetchall()
    return data































def delete_Employee(Emp_id):
    c.execute('DELETE FROM Employee WHERE Emp_id="{}"'.format(Emp_id))
    mydb.commit()

def delete_payroll(transaction_id):
    c.execute('DELETE FROM payroll WHERE transaction_id="{}"'.format(transaction_id))
    mydb.commit()

def delete_paygrade(grade_id):
    c.execute('DELETE FROM paygrade WHERE grade_id="{}"'.format(grade_id))
    mydb.commit()

def delete_department(department_id):
    c.execute('DELETE FROM department WHERE department_id="{}"'.format(department_id))
    mydb.commit()












def loan(x):
    c.execute('SELECT "{}" from payroll'.format(x))
    data = c.fetchall()
    return data


def joining():
    c.execute('SELECT payroll.Emp_id, Employee.bank_name,payroll.transaction_id,Employee.city,payroll.loan,Employee.fname,payroll.Emp_net_sal FROM payroll JOIN Employee ON payroll.Emp_id = Employee.Emp_id;')
    data = c.fetchall()
    return data

def joining_2():
    c.execute('SELECT department.department_id,department.department_name, paygrade.grade_id, paygrade.grade_name, paygrade.grade_bonus  FROM paygrade JOIN department ON paygrade.department_id= department.department_id;')
    data = c.fetchall()
    return data

def joining_3():
    c.execute('SELECT department.department_id, Employee.Emp_id, Employee.fname,Employee.lname FROM Employee JOIN department ON Employee.department_id=department.department_id')
    data = c.fetchall()
    return data











def union_1():
    c.execute('SELECT payroll.Emp_id FROM payroll UNION SELECT Employee.Emp_id FROM Employee ')
    data = c.fetchall()
    return data

def intersection_1():
    c.execute('SELECT payroll.Emp_id FROM payroll INTERSECT SELECT Employee.Emp_id FROM Employee ')
    data = c.fetchall()
    return data

def aggregate():
    c.execute('SELECT bank_name, COUNT(bank_name) FROM Employee GROUP BY bank_name;')
    data = c.fetchall()
    return data


def aggregate_2():
    c.execute('SELECT MIN(loan) highest_loan FROM Employee JOIN payroll USING (Emp_id);')
    #c.execute('SELECT Employee.fname, MIN(loan) LEAST_loan FROM Employee JOIN payroll ON (Employee.Emp_id=payroll.Emp_id) WHERE payroll.loan=MIN(loan);')
    data = c.fetchall()
    return data

def aggregate_3():
    c.execute('SELECT MAX(loan) highest_loan FROM Employee JOIN payroll USING (Emp_id);')
    data = c.fetchall()
    return data

def query_1(x):
    c.execute(x)
    data = c.fetchall()
    return data

def info():
    c.execute('SELECT * FROM employee_email2;')
    data = c.fetchall()
    return data

def infop():
    c.execute('SELECT * FROM tax_table;')
    data = c.fetchall()
    return data






