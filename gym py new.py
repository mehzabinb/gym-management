import mysql.connector as sql

conn=sql.connect(host="localhost", user="root", passwd="", database="fitness")
db=conn.cursor()
'''if conn.is_connected():
    print("Conection With Database Establised Successfully")
else:
    print("Conection With Database Failed ")'''

print("************************Welcome to GOLD FITNESS CENTRE************************")
db=conn.cursor()
choice = 0
while (True):
    print("1.CREATE YOUR ACCOUNT")
    print("2.LOG IN")
    print("3.EXIT")
    choice=int(input("ENTER YOUR CHOICE:"))
    
    if choice ==1:
     cust_name=input("Enter your name : ")
     account_no=int(input("enter your User ID :"))
     password=int(input("Enter your Password :"))
     SQL_insert="insert into Log_in values ('"+cust_name+"',"+str(account_no)+","+str(password)+")"
     db.execute(SQL_insert)
     conn.commit()
     print("ACCOUNT CREATED")

    if choice==2:
     print('')
     print('Enter your Credentials')
     cust_name=input('Enter your name : ')
     print('')
     account_no=int(input('Enter your User ID : '))
     print(' ')
     password=int(input('Enter your Password : '))
     print(' ')
     #db=conn.cursor()
     db.execute('select * from Log_in')
     data=db.fetchall()
     count=db.rowcount
     #c2 = 0
     for row in data:
      if (cust_name in row) and (account_no in row) and (password in row):
            print(' ')
            print(' ')
            print("************************WELCOME TO GOLD FITNESS CENTRE************************")
            print(' ')
            print(' ')
            print('TO SEE TRAINERS DETAILS,press                :1')
            print(' ')
            print('TO UPDATE NAME DETAILS,press                  :2')
            print(' ')
            print('TO UPDATE PAYMENT DETAILS,press               :3')
            print(' ')
            print('TO SEE DETAILS OF ALL THE CUSTOMERS,press     :4')
            print(' ')
            print('TO ENTER NEW CUSTOMER DETAILS,press           :5')
            print(' ')
            print('TO EXIT,press                                 :6')
            print(' ')
            print('WANT TO RATE US,press                         :7')
            print(' ')
            c2=int(input("Enter your choice : "))
            if (c2==1):
                db=conn.cursor()
                db.execute('select * from log_in')
                data=db.fetchall()
                count=db.rowcount
                print('Details of all trainers ',count)
                print("Details of all trainers are arranged as Name/User ID/Password")
                for row in data:
                    print(row)
                conn.commit()    
                print("VISIT AGAIN")
            elif (c2==2):
                print('')
                print('TO UPDATE FILL THIS')
                print('')
                empName = input("Enter name : ")
                update = input("Enter new name : ")
                sqlFormula = "UPDATE log_in SET cust_name=%s WHERE cust_name = %s"
                db.execute(sqlFormula,(update,empName))
                conn.commit()
                print('YOUR DETAILS ARE SUCESSFULLY UPDATED')

            elif (c2==3):
                print('')
                print('TO UPDATE PAYMENT FILL THIS')
                print('')
                custPayment= input("Enter name : ")
                update = input("Enter new Payment : ")
                sqlFormula = "UPDATE gym SET Payment=%s WHERE cust_name= %s"
                db.execute(sqlFormula,(update,custPayment))
                conn.commit()
                print('YOUR DETAILS ARE SUCESSFULLY UPDATED')

            elif(c2==4):
                  db=conn.cursor()
                  db.execute('select * from gym ')
                  data=db.fetchall()
                  count=db.rowcount
                  print('Details of all the Customers',count)
                  for row in data:
                     print(row)
                  print("VISIT AGAIN")

            elif(c2==5):
                 f_name=input("Enter the your name : ")
                 price=int(input("Enter the amount to be paid : "))
                 Payment=input("Enter If the amount is Paid/Half paid : ")
                 wieght=int(input("enter your customer weight : "))
                 cust_name=input("enter Customer Name : ")
                 gender=input("Enter Customer gender of customer : ")
                 SQL_insert="insert into gym values('"+ f_name+"','"+str(price)+"','"+Payment+"','"+str(wieght)+"','"+cust_name+"','"+gender+"')"
                 db.execute(SQL_insert)
                 conn.commit()
                 print("Bill Recorded")

            elif (c2==6):
                  print('THANK YOU FOR VISITING')
            

            elif (c2==7):
                print('RATE US FOR SERVICE')
                rating=int(input("On the Scale of 10 how would you like to rate us:"))
                print('THANK YOU FOR RATING')
            else:
                print("Oops, something went wrong.....")
                db.close()
                
    if choice==3:
        print("THANK YOU FOR VISITING")
        db.close()
               
                 
            
