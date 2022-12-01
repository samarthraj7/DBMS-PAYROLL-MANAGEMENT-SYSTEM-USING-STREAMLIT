create table Employee(Emp_id varchar(10),
					fname varchar(15) NOT NULL,
                    lname varchar(15) NOT NULL,
                    dob varchar(30)  NOT NULL,
                    phone varchar(10) NOT NULL ,
                    email varchar(40) NOT NULL,
                    country varchar(20) NOT NULL,
					city varchar(30),
					pincode int(6),
                    bank_name varchar(20) NOT NULL,
					department_id varchar(10) NOT NULL,
                    primary key(Emp_id),
					FOREIGN KEY (department_id) REFERENCES department(department_id) ON DELETE CASCADE);


create table payroll(transaction_id varchar(20)  NOT NULL,
					Emp_id varchar(20)   NOT NULL,
					account_no varchar(20)  NOT NULL,
					bank_name varchar(30)   NOT NULL,
					Emp_net_sal varchar(20) NOT NULL,
					Emp_sal_yr varchar(20) NOT NULL,
					Reinbursment_date varchar(20) NOT NULL,
					loan varchar(10) default NULL,
					grade_id varchar(10) NOT NULL,
					primary key(transaction_id),
					FOREIGN KEY (grade_id) REFERENCES paygrade(grade_id) ON DELETE CASCADE,
					FOREIGN KEY (Emp_id) REFERENCES employee(Emp_id) ON DELETE CASCADE);



create table paygrade(grade_id varchar(10),
					grade_name varchar(30) NOT NULL,
					grade_basic varchar(30) NOT NULL,
					grade_bonus varchar(30) NOT NULL,
					department_id varchar(10) NOT NULL,
					primary key(grade_id),
					FOREIGN KEY (department_id) REFERENCES department(department_id) ON DELETE CASCADE);
	

create table department(department_id varchar(10),
								department_name varchar(30),
								primary key (department_id,department_name));







------------------------- PROCEDURE ----------------------
DELIMITER $$
CREATE PROCEDURE getemployee_admin(in Emp_id int)
    BEGIN
    select fname, lname
    from employee WHERE employee.Emp_id = Emp_id;
    end $$
delimiter ;
CALL getemployee_admin(1);

---------------------- CURSER ---------------------------------
CREATE TABLE EMPLOYEE_EMAIL(
    fname varchar(20),
    lname varchar(20),
    email VARCHAR(50)
);

DELIMITER $$
CREATE PROCEDURE create_email ()
BEGIN
	DECLARE done INTEGER DEFAULT 0;
    DECLARE b_fname varchar(15) ;
    DECLARE b_lname varchar(15) ;
	DECLARE b_email varchar(40) ;
	DEClARE curemail CURSOR FOR SELECT fname, lname, email FROM employee;
	DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;

	OPEN curEmail;

	LABLE: LOOP
	FETCH curemail INTO b_fname, b_lname, b_email;
	IF done = 1 THEN 
	LEAVE LABLE;
	END IF;
	INSERT INTO EMPLOYEE_EMAIL VALUES(b_fname, b_lname, b_email);
	END LOOP;

	CLOSE curemail;
END$$

DELIMITER ;
CALL create_email();

---------------------------- FUNCTION -------------------------------

DELIMITER $$
CREATE FUNCTION `loan`(balance int) RETURNS varchar(50)
    DETERMINISTIC
BEGIN
DECLARE VALUE varchar(50);

IF balance<10000 then
set VALUE="no";

ELSE
set VALUE ="yes";

end if;

return value;
END$$
DELIMITER ;

-------------------------- TRIGGER ---------------------


DELIMITER $$
CREATE TRIGGER loan_validation1
BEFORE INSERT 
ON payroll 
FOR EACH ROW
BEGIN
    DECLARE error_msg VARCHAR(300);
    SET error_msg = ("No You cant ask for more than 10000 initial loan!!! its not ACCEPTABLE!");
    IF new.loan > 10000 THEN 
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = error_msg;
    END IF;
END $$
DELIMITER ;


------------------------------------------------------------------

DELIMITER $$
CREATE FUNCTION `loan`(balance int) RETURNS varchar(50)
    DETERMINISTIC
BEGIN
DECLARE VALUE varchar(50);

IF balance<10000 then
set VALUE="no";

ELSE
set VALUE ="yes";

end if;

return value;
END$$
DELIMITER ;


-------------------- CURSER TO IMPLEMENT THE GROSS SALARY OF THE EMPLOYEE---------------------

CREATE TABLE tax_table(
    fname varchar(20),
    tax varchar(20),
	loan varchar(20),
	Emp_net_sal varchar(20),
    final_sal VARCHAR(50)
);
DELIMITER $$
CREATE PROCEDURE tax_t()
BEGIN
	DECLARE done INTEGER DEFAULT 0;
    DECLARE b_fname varchar(15) ;
    DECLARE b_tax varchar(15) ;
	DECLARE b_loan varchar(40) ;
	DECLARE b_Emp_net_sal varchar(20) ;
	DECLARE b_final_sal varchar(20) ;
	DEClARE curetax CURSOR FOR select fname, Emp_net_sal * 0.30 as tax ,(loan-(loan*0.1))as loan, Emp_net_sal, Emp_net_sal-(Emp_net_sal * 0.30)-(loan*0.1) as final_sal
    FROM payroll JOIN Employee ON payroll.Emp_id = Employee.Emp_id
	where Employee.Emp_id=Empi_id;
	DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;

	OPEN curetax;

	LABLE: LOOP
	FETCH curtax INTO b_fname, b_tax, b_loan,b_Emp_net_sal, b_final_sal;
	IF done = 1 THEN 
	LEAVE LABLE;
	END IF;
	INSERT INTO tax_table VALUES(b_fname, b_tax, b_loan,b_Emp_net_sal, b_final_sal);
	END LOOP;

	CLOSE curetax;
END$$

DELIMITER ;
CALL tax_t();


----------------------------------------------- END ----------------------------------------

