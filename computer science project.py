#connecting MySQL with python
import mysql.connector as ms
con=ms.connect(host='localhost',user='root',password="Shivansh#06")
cur=con.cursor()


#to create a database named school
try:
    cur.execute("Create database school")
    print("Database created")
except:
    print("Database already exists")
cur.execute("Use school")

#to create a table named class
try:
    sql='''CREATE TABLE student_records(NAME VARCHAR(30),
                                    ADMISSION_NUMBER INT PRIMARY KEY,
                                    CLASS VARCHAR(2), SECTION CHAR(1),
                                    ROLL_NUMBER INT(2) NOT NULL,
                                    BLOOD_GROUP VARCHAR(2),
                                    DATE_OF_BIRTH DATE,
                                    AGE INT(2),
                                    EMAIL VARCHAR(30),
                                    STREAM VARCHAR(10));'''
    cur.execute(sql)
    print("Table student_records is created")
except:
    print('table already exists')

#to insert information into table created above
def insert():
    name=input('enter name of student:-')
    adm=int(input('enter admission number:-'))
    cl=input('enter class:-')
    sec=input('enter section:-')
    rno=int(input('enter roll no.:-'))
    bg=input('enter blood group:-')
    dob=input('enter date of birth:-')
    age=int(input('enter age of student:-'))
    eml=input('enter email id:-')
    stre=input('enter stream of student:-')
    try:
        sql="INSERT INTO student_records VALUES('{}',{},'{}','{}',{},'{}','{}',{},'{}','{}');".format(name,adm,cl,sec,rno,bg,dob,age,eml,stre)
        cur.execute(sql)
        con.commit()
        sql="SELECT COUNT(*) FROM student_records;"
        cur.execute(sql)
        r=cur.fetchall()
        print(r, "items in stacks")
    except Exception as e:
        print(e)
        
#to update information present in the table
def update():
    print('what do you want to update?')
    print('1.name of student')
    print('2.class of student')
    print('3.section of student')
    print('4.roll no. of student')
    print('5.blood group')
    print('6.date of birth')
    print('7.age of student')
    print('8.email of student')
    print('9.stream of student')
    ch=int(input('enter choice:-'))
    if ch==1:
        nm=input('enter existing name of student:-')
        nnm=input('enter new name of student:-')
        adm=int(input('enter admission number:-'))
        try:
            sql="UPDATE student_records SET NAME={} WHERE ADMISSION_NUMBER={};".format(nnm,adm)
            cur.execute(sql)
            con.commit()
            print(cur.rowcount,"record updated")
        except Exception as e:
            print(e)

    if ch==2:
        nm=int(input('enter existing class of student:-'))
        nnm=int(input('enter new class of student:-'))
        adm=int(input('enter admission number:-'))
        try:
            sql="UPDATE student_records SET CLASS={} WHERE ADMISSION_NUMBER={};".format(nnm,adm)
            cur.execute(sql)
            con.commit()
            print(cur.rowcount,"record updated")
        except Exception as e:
            print(e)

    if ch==3:
        nm=input('enter existing section of student:-')
        nnm=input('enter new section of student:-')
        adm=int(input('enter admission number:-'))
        try:
            sql="UPDATE student_records SET SECTION={} WHERE ADMISSION_NUMBER={};".format(nnm,adm)
            cur.execute(sql)
            con.commit()
            print(cur.rowcount,"record updated")
        except Exception as e:
            print(e)

    if ch==4:
        nm=int(input('enter existing roll number of student:-'))
        nnm=int(input('enter new roll number of student:-'))
        adm=int(input('enter admission number:-'))
        try:
            sql="UPDATE student_records SET ROLL_NUMBER={} WHERE ADMISSION_NUMBER={};".format(nnm,adm)
            cur.execute(sql)
            con.commit()
            print(cur.rowcount,"record updated")
        except Exception as e:
            print(e)

    if ch==5:
        nm=input('enter existing blood group of student:-')
        nnm=input('enter new blood group of student:-')
        adm=int(input('enter admission number:-'))
        try:
            sql="UPDATE student_records SET BLOOD_GROUP={} WHERE AND ADMISSION_NUMBER={};".format(nnm,adm)
            cur.execute(sql)
            con.commit()
            print(cur.rowcount,"record updated")
        except Exception as e:
            print(e)

    if ch==6:
        nm=input('enter existing date of birth of student:-')
        nnm=input('enter new date of birth of student:-')
        adm=int(input('enter admission number:-'))
        try:
            sql="UPDATE student_records SET DATE_OF_BIRTH={} WHERE ADMISSION_NUMBER={};".format(nnm,adm)
            cur.execute(sql)
            con.commit()
            print(cur.rowcount,"record updated")
        except Exception as e:
            print(e)
            
    if ch==7:
        nm=int(input('enter existing age of student:-'))
        nnm=int(input('enter new age of student:-'))
        adm=int(input('enter admission number:-'))
        try:
            sql="UPDATE student_records SET AGE={} WHERE ADMISSION_NUMBER={};".format(nnm,adm)
            cur.execute(sql)
            con.commit()
            print(cur.rowcount,"record updated")
        except Exception as e:
            print(e)

    if ch==8:
        nm=input('enter existing email of student:-')
        nnm=input('enter new email of student:-')
        adm=int(input('enter admission number:-'))
        try:
            sql="UPDATE student_records SET EMAIL={} WHERE ADMISSION_NUMBER={};".format(nnm,adm)
            cur.execute(sql)
            con.commit()
            print(cur.rowcount,"record updated")
        except Exception as e:
            print(e)

    if ch==9:
        nm=input('enter existing stream of student:-')
        nnm=input('enter new stream of student:-')
        adm=int(input('enter admission number:-'))
        try:
            sql="UPDATE student_records SET STREAM={} WHERE ADMISSION_NUMBER={};".format(nnm,adm)
            cur.execute(sql)
            con.commit()
            print(cur.rowcount,"record updated")
        except Exception as e:
            print(e)

    
#to delete information from table
def delete():
    adm=int(input('enter admission number of student whose details are to be deleted:-'))
    try:
        sql="DELETE FROM student_records WHERE ADMISSION_NUMBER={};".format(adm)
        cur.execute(sql)
        con.commit()
        print(cur.rowcount,'record deleted')
    except Exception as e:
        print(e)
        con.rollback()
	 
#to display information of individual student
def idisplay():
    adm=input('enter admission number of student whose details are to be displayed:-')
    sql='SELECT * FROM student_records WHERE ADMISSION_NUMBER={};'.format(adm)
    cur.execute(sql)
    v=cur.fetchall()
    for i in v:
        print(i)

# to display the information of all the students present in table
def display():
    sql="SELECT * FROM student_records;"
    cur.execute(sql)
    v=cur.fetchall()
    for i in v:
        print(i)

#to display names starting from any alphabet
def ndisplay():
    a=input('enter alphabet from which the name starts:-')
    sql="SELECT * FROM student_records WHERE NAME LIKE '{}%'".format(a)
    cur.execute(sql)
    v=cur.fetchall()
    for i in v:
        print(i)

#to display student information classwise
def cdisplay():
    cl=int(input('enter class whose information you want to see:-'))
    s=input('enter section of that class:-')
    sql="SELECT * FROM student_records WHERE CLASS={} AND SECTION='{}';".format(cl,s)
    cur.execute(sql)
    v=cur.fetchall()
    for i in v:
        print(i)
    


#MAIN MENU
while True:
    print('1.add item to STUDENT_RECORDS')
    print('2.update student details')
    print('3.delete student details')
    print('4.display individual student details')
    print('5.display all details of student')
    print('6.display name of all students starting from an alphabet')
    print('7.display student information of a particular class')
    print('8.exit menu')
    ch=input('enter choice:-')
    if ch=='1':
        while True:
            insert()
            ch1=input('do you wish to continue? y/Y n/N')
            if ch1 in 'nN':
                break
    if ch=='2':
        while True:
            update()
            ch1=input('do you wish to continue? y/Y n/N')
            if ch1 in 'nN':
                break
    if ch=='3':
        while True:
            delete()
            ch1=input('do you wish to continue? y/Y n/N')
            if ch1 in 'nN':
                break
    if ch=='4':
        while True:
            idisplay()
            ch1=input('do you wish to continue? y/Y n/N')
            if ch1 in 'nN':
                break
    if ch=='5':
        while True:
            display()
            ch1=input('do you wish to continue? y/Y n/N')
            if ch1 in 'nN':
                break
    if ch=='6':
        while True:
            ndisplay()
            ch1=input('do you wish to continue? y/Y n/N')
            if ch1 in 'nN':
                break
    if ch=='7':
        while True:
            cdisplay()
            ch1=input('do you wish to continue? y/Y n/N')
            if ch1 in 'nN':
                break
    if ch=='8':
        break


