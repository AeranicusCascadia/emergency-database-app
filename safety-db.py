import sqlite3
import tkinter

# create database
db = sqlite3.connect('database')

# Create cursor object
cursor = db.cursor()

# globals
last_name = ""
first_name = ""
floor = 0
warden_zone = 0
mob_ass = "no"
med_needs = "no"

def close_database():
	db.close

def create_staff_table():
	# try to create staff table
	try:
		
		cursor.execute('''
			CREATE TABLE staff(staff_id INTEGER PRIMARY KEY AUTOINCREMENT, last_name TEXT, first_name TEXT, floor INTEGER, \
			warden_zone INTEGER, mobility_assistance TEXT, medical_needs TEXT)
		''')
		
		print('Creating staff table in database.')
		
	except:
		# message if table exists
		print('staff table already exists.')
		
		

def insert_test_data(last_name, first_name, floor, warden_zone, mob_ass, med_needs):
# insert dest data into staff table

	# insert info into staff table
	cursor.execute('''INSERT INTO staff(last_name, first_name, floor, warden_zone, mobility_assistance, medical_needs)
					VALUES(?,?,?,?,?,?)''',(last_name, first_name, floor, warden_zone, mob_ass, med_needs))
	
	# commit to database
	db.commit()
	
	# Message to user
	print('Data inserted into staff table.')
	
def insert_data(last_name, first_name, floor, warden_zone, mob_ass, med_needs):
	pass
	
def poplulate_db_from_phonelist():
	pass
	
def display_all_rows():
	
	# execute select query
	cursor.execute('''SELECT staff_id, last_name, first_name, floor, warden_zone, mobility_assistance, medical_needs FROM staff''')
	
	# pass fetchall (rows) method to var: all_rows
	all_rows = cursor.fetchall()
	
	# Just a little formatting, etc
	print('')
	print('Emergency information for staff:')
	print('-------------------------------')
	
	# iterate through every row
	for row in all_rows:
		# print data in every column
		print(f'{row[0]})  {row[1]}, {row[2]}. floor: {row[3]}. warden zone: {row[4]}. assistance? {row[5]}. meds? {row[6]}')

	
	


create_staff_table()

insert_test_data("Doe", "Jane", 1, 1, "no", "no")
insert_test_data("Spade", "Sam", 3, 5, "yes", "insulin")
insert_test_data("Gomez", "Sal", 2, 3, "no", "no")
insert_test_data("Washington", "Kaylee", 2, 3, "yes", "wheelchair")

display_all_rows()




