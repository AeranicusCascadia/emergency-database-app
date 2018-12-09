import sqlite3
import tkinter

# create database
db = sqlite3.connect('database')

# Create cursor object
cursor = db.cursor()

# globals
curr_last_name = ""
curr_first_name = ""
curr_floor = 0
curr_warden_zone = 0
curr_mob_ass = 0
curr_med_needs = "no"

# create staff table
def create_staff_table():
	
	try:
		
		cursor.execute('''
			CREATE TABLE staff(staff_id INTEGER PRIMARY KEY AUTOINCREMENT, last_name TEXT, first_name TEXT, floor INTEGER, \
			warden_zone INTEGER, mobility assistance INTEGER, medical_needs TEXT)
		''')
		
		print('Creating staff table in database.')
		
	except:
		print('staff table already exists.')
		



create_staff_table()
