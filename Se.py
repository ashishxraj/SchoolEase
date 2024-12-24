
import sqlite3
con = sqlite3.connect("SCHOOL")
cursor = con.cursor()

#create student table 
cursor.execute('''
               CREATE TABLE IF NOT EXISTS student(
               StudentID INT PRIMARY KEY, 
               Name TEXT NOT NULL,
               Class TEXT NOT NULL,
               Rollno INT NOT NULL,
               Address TEXT,
               Phone INT );''')

#create teacher table
cursor.execute('''
               CREATE TABLE IF NOT EXISTS teacher(
               StaffID INT PRIMARY KEY,
               Name TEXT NOT NULL,
               Post TEXT NOT NULL,
               Salary INT ,
               Address TEXT,
               Phone INT NOT NULL,
               Accountno TEXT NOT NULL);''')

#create student attendance table
cursor.execute('''CREATE TABLE IF NOT EXISTS student_attendance_details (
    Date TEXT NOT NULL,
    Name Text NOT NULL,   
    Class TEXT NOT NULL,
    StudentID INT NOT NULL,
    Absent BOOLEAN NOT NULL
);''')


#create teacher attendance table
cursor.execute('''
               CREATE TABLE IF NOT EXISTS teacher_attendance(
               Date TEXT NOT NULL,
               Absent TEXT NOT NULL );''')

#create salary table
cursor.execute('''
               CREATE TABLE IF NOT EXISTS salary(
               Name TEXT NOT NULL,
               Month TEXT NOT NULL,
               Salary INT NOT NULL );''')

con.commit()

#funtion to add student
def add_student():
    name = input("Student Name: ")
    cls =input("Class Name: ")
    rollno = input("Roll No:")
    address = input("Address:")
    phone = input("Phone:")
    studentID = input("Student ID : ")
    data = (name,cls,rollno,address,phone,studentID)
    sql = "INSERT INTO student VALUES(?,?,?,?,?,?)"
    cursor = con.cursor()
    cursor.execute(sql, data)
    con.commit()
    print("Data Entered Successfully")
    print(">------------------------------------------------------------<")

#function to remove student
def remove_student():
    name = input("student name :")
    studentID= input("StudentID : ")
    data = (name,studentID)
    sql = "DELETE FROM student WHERE studentID = ?;"
    cursor = con.cursor()
    cursor.execute(sql,data)
    con.commit()
    print("Data Updated successfully")
    print(">------------------------------------------------------------------<")

#function to add teacher
def add_teacher():
    name = input(" Enter teacher name:")
    post = input(" Enter post:")
    salary = input("Enter salary:")
    address = input("Enter address:")
    phone = input("Enter phone number:")
    accountno = input("Enter account number:")
    staffID = input("Staff ID: ")
    data = (name, post, salary, address, phone, accountno, staffID)
    sql = "INSERT INTO teacher VALUES(?,?,?,?,?,?,?)"
    cursor = con.cursor()
    cursor.execute(sql,data)
    con.commit()
    print("Data Entered Successfully.")
    print(">----------------------------------------------------------------------<")

#function to remove teacher
def remove_teacher():
    name = input("Teacher Name : ")
    staffID = input("Staff ID : ")
    data = (name,staffID)
    sql = "DELETE FROM teacher WHERE name = ? and staffID = ?"
    cursor = con.cursor()
    cursor.execute(sql,data)
    con.commit()
    print("Data Updated")
    print(">----------------------------------------------------------------------<")

#function to mark absent students
def abclass():
    date = input("Date : ")
    cls = input("Class : ")
    absent = input("Names of Absent Students : ")
    data = (date,cls,absent)
    sql ="INSERT INTO cattendance VALUES(?, ?, ?)"
    cursor = con.cursor()
    cursor.execute(sql,data)
    con.commit()
    print("Data Updated.")
    print(">----------------------------------------------------------------------<")

#function to mark absent teacher
def abteacher():
    date = input("Date : ")
    absent = input("Names of Absent Teacher : ")
    data = (date,absent)
    sql = "INSERT INTO tattendance VALUES(?,?)"
    cursor = con.cursor()
    cursor.execute(sql,data)
    con.commit()
    print("Data Updated")
    print(">---------------------------------------------------------------------<")

#function to update faculty salary details
def pays():
    name = input("Teacher Name : ")
    month = input("Month :")
    salary= input ("salary :")
    data = (name,month)
    sql = "INSERT INTO salary VALUES(?,?,?)"
    cursor = con.cursor()
    cursor.execute(sql,data)
    con.commit()
    print("Data Entered Successfully.")
    print(">------------------------------------------------------------------<")


def display_class():
    cls = input("Class : ")
    data = (cls,)
    sql = "SELECT * FROM student WHERE class = ?"
    cursor = con.cursor()
    cursor.execute(sql,data)
    d = cursor.fetchall()
    for i in d:
        print("StudentID : ",i[0])
        print("NAME : ",i[1])
        print("CLASS : ",i[2])
        print("ROLL : ",i[3])
        print("ADDRESS : ",i[4])
        print("PHONE : ",i[5])
        print(">--------------------------------------------------------------<")


def display_teacher():
    sql = "SELECT * FROM teacher"
    cursor = con.cursor()
    cursor.execute(sql)
    d =cursor.fetchall()
    for i in d:
        print("StaffID : ",i[0])
        print("NAME : ",i[1])
        print("POST : ",i[2])
        print("SALARY : ",i[3])
        print("ADDRESS : ",i[4])
        print("PHONE : ",i[5])
        print("ACNO : ",i[6])
        print(">----------------------------------------------------------------<")

def main():
    print("""                 Rajkiya Pratibha Vikas Vidyalaya
                                  BE- Block, Hari Nagar
                1. Add student
                2. Remove student
                3. Add teacher
                4. Remove teacher
                5. CLASS ATTENDANCE
                6. TEACHER ATTENDANCE
                7. PAY SALARY
                8. DISPLAY CLASS
                9. TEACHERS LIST """)
    choice = input("Enter Task No : ")
    print(">--------------------------------<")
    if (choice == '1'):
        add_student()
    elif (choice=='2'):
        remove_student()
    elif (choice=='3'):
        add_teacher()
    elif (choice=='4'):
        remove_teacher()
    elif (choice=='5'):
        abclass()
    elif (choice == '6'):
        abteacher()
    elif (choice == '7'):
        pays()
    elif (choice == '8'):
        display_class()
    elif (choice == '9'):
        display_teacher()
    else:
        print(" Wrong choice.......")
    
main()

con.close()