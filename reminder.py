import sqlite3
import subprocess as sp   
import sys   
db=sqlite3.connect('rem.db')
cur=db.cursor()
def startpgm():
	print("\n\nWelcome to Reminder Chart!\nPress any of the option below\n  1 - For create table 'reminder'\n  2 - For create reminders\n  3 - For view all reminders\n  4 - For update a reminder\n 5 - Exit")
	inp = input('Enter your option : ')
	if inp == '1':

		
		
		try:        
		    cur =db.cursor()
		    cur.execute('''CREATE TABLE reminder (
		    reminderID INTEGER PRIMARY KEY AUTOINCREMENT,
		    reminderTitle TEXT (20) NOT NULL,
		    reminderDateTime TEXT (20) NOT NULL);''')
		    print ('Reminder table created successfully')
		except:
		    print ('Error in Reminder table creation')
		    db.rollback()
		startpgm()
	elif inp == '2':
		
		reminderTitle = input('\nEnter reminder title : ')
		reminderDateTime = input('\nEnter reminder time in DD/MM/YYYY HH:MM:SS format : ')
		qry="insert into reminder (reminderTitle, reminderDateTime) values('"+reminderTitle+"', '"+reminderDateTime+"');"
		try:
		    cur=db.cursor()
		    cur.execute(qry)
		    db.commit()
		    print ("\nOne reminder added successfully")
		except:
		    print ("\nError in addition")
		    db.rollback()
		startpgm()
	
	elif inp == '3':
		
		print("\n")
		sql="SELECT * from reminder;"
		cur=db.cursor()
		cur.execute(sql)
		flag=False
		listData=cur.fetchall()
		for x in listData:
			flag = True
			print(x)
		if flag == False:
			print("\nNo records found")
		
		startpgm()
	elif inp == '4':
		reminderID = input('\nEnter reminder Id : ')
		reminderTitle = input('\nEnter new reminder title : ')
		reminderDateTime = input('\nEnter new reminder time in DD/MM/YYYY HH:MM:SS format : ')
		qry="update reminder set reminderTitle=?,reminderDateTime=? where reminderID=?;"
		try:
		    cur=db.cursor()
		    cur.execute(qry, (reminderTitle,reminderDateTime,reminderID))
		    db.commit()

		    print("\nReminder updated successfully")
		except:
		    print("\nError in operation")
		    db.rollback()
		startpgm()
	elif inp == '5':
		db.close()
		print("Thank you, see you again")
		sys.exit()
	else:
		print("Invalid Input, Please try again!!!")
		#startpgm()
startpgm()
