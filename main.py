# GUI build of staff emergency database application

import sqlite3
from tkinter import *
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox

# create database
db = sqlite3.connect('database')

# Create cursor object
cursor = db.cursor()

# class to handle application data
class DataObject:
	def __init__(self, fetched_data, pre_message, target_var, last_name, first_name, floor, warden_zone, mob_ass, med_needs):
		self.fetched_data = fetched_data
		self.pre_message = pre_message
		self.target_var = target_var
		self.last_name = last_name
		self.first_name = first_name
		self. floor = floor
		self.warden_zone = warden_zone
		self.mob_ass = mob_ass
		self.med_needs = med_needs
		
# Our sole instance of DataObject class
current_data = DataObject('Default fetched data', 'Default pre-message', None, 'default last name'\
, 'default first name', 0, 0, 'no', 'no')

# File --> Exit
def client_exit():
	exit()

# create and define root window
window = Tk()
window.title("Database Manager: CPM staff emergency information")
window.geometry('800x700')

menu = Menu(window) # add menu (automatically goes on top bar in root window

window.config(menu=menu) # attach the menu to root window

# ROW 0:

# text area created early so functions defined below can target it
main_display = scrolledtext.ScrolledText(window,width=95,height=25) # create scroll text box
main_display.grid(row=0, column=0, columnspan=5, padx=5, pady=10) # place scroll text box by grid coordinate
main_display.config(state = 'disabled') # start disabled. enable through appropriate functions

# ROW 1:
# create and place label for application messages field
message_display_label = Label(window, text=' Applicaion Messages: ', bg="green", fg="white", font=("Arial Bold", 9))
message_display_label.grid(column=0,row=1, columnspan=5, padx=10, pady=15, sticky=W)
	
# ROW 2:
# create field for application messages to user
message_display = Text(window, width=80, height=5)
message_display.grid(row=2, column=0, columnspan=3, padx=10, pady=10)
message_display.config(state = 'disabled') # field initially disabled

# ROW 3:
new_entry_label = Label(window, text=' Fields for new entry information: ', \
bg="green", fg="white", font=("Arial Bold", 9))
new_entry_label.grid(row=3, column=0, columnspan=5, padx=10, pady=15, sticky=W)

# ROW 4:
field_last_name = Entry(window, width=20)
field_last_name.grid(row=4, column=1, columnspan=2, padx=15, pady=15)
field_last_name_label = Label(window, text='Last Name: ', bg="white", fg="blue", font=("Arial Bold", 9))
field_last_name_label.grid(row=4, column=0, padx=10, sticky=W)
	
def display_numeric():
	
	# enable text field and clear it
	main_display.config(state = 'normal')
	main_display.delete(1.0, END)
	
	#execute select query, default sort by primary key
	cursor.execute('''SELECT staff_id, last_name, first_name, \
	floor, warden_zone, mobility_assistance, medical_needs FROM staff''')
	
	# pass fetchall (rows) method to var: all_rows
	all_rows = cursor.fetchall()
	
	for row in all_rows:
		# display with staff_id leading
		content = f' {row[0]})  {row[1]}, {row[2]} | Floor: {row[3]} | Warden Zone: {row[4]} | Assistance: {row[5]} | Med: {row[6]}'
		
		main_display.insert(INSERT, content + '\n')
		
	# disable text field to be read-only
	main_display.config(state = 'disabled')
	
	# Print to console for testing
	print('display_numeric')
	
	
def display_alphabetic():
	
	# enable text field and clear it
	main_display.config(state = 'normal')
	main_display.delete(1.0, END)

	#execute select query, default sort by primary key
	cursor.execute('''SELECT staff_id, last_name, first_name, floor, warden_zone, \
	mobility_assistance, medical_needs FROM staff\
	ORDER BY last_name''')
	
	# pass fetchall (rows) method to var: all_rows
	all_rows = cursor.fetchall()
	
	for row in all_rows:
		# display with staff_id leading
		content = f' {row[1]}, {row[2]} | Floor: {row[3]} | Warden Zone: {row[4]} | Assistance: {row[5]} | Med: {row[6]}'
		
		main_display.insert(INSERT, content + '\n')
		
	# disable text field to be read-only
	main_display.config(state = 'disabled')

	# Print to console for testing
	print('display_alphabetic')

def create_staff_table():
	# try to create staff table
	try:
		
		cursor.execute('''
			CREATE TABLE staff(staff_id INTEGER PRIMARY KEY AUTOINCREMENT, last_name TEXT, first_name TEXT, floor INTEGER, \
			warden_zone INTEGER, mobility_assistance TEXT, medical_needs TEXT)
		''')
		
		print('create_staff_table --> created table')
		
	except:
		# message if table exists
		print('create_staff_table --> attempted to create staff table, but it already exists.')	

def insert_data(last_name, first_name, floor, warden_zone, mob_ass, med_needs):
# insert dest data into staff table

	# insert info into staff table
	cursor.execute('''INSERT INTO staff(last_name, first_name, floor, warden_zone, mobility_assistance, medical_needs)
					VALUES(?,?,?,?,?,?)''',(last_name, first_name, floor, warden_zone, mob_ass, med_needs))
	
	# commit to database
	db.commit()
	
	# Print to console for testing
	print('insert_data')
	
def insert_test_data():
	insert_data("Doe", "Jane", 1, 1, "no", "no")
	insert_data("Spade", "Sam", 3, 5, "yes", "insulin")
	insert_data("Gomez", "Sal", 2, 3, "no", "no")
	insert_data("Washington", "Kaylee", 2, 3, "yes", "wheelchair")
	insert_data("Chang", "Sarah", 3, 6, "no", "no")
	insert_data("Jennings", "Robert", 1, 2, "yes", "cast (arm)")
	insert_data("Goldsmith", "Chloe", 2, 4, "no", "no")
	insert_data("Brown", "Marvin", 2, 5, "no", "no")
	
	# Print to console for testing.
	print('insert_test_data')
	
def update_floor(l_name, f_name, new_data):
	
	# Execute SQL
	cursor.execute('''UPDATE staff SET floor = ? WHERE last_name = ? AND first_name = ?'''\
	,(new_data, l_name, f_name,))
	
	# Commit changes to database
	db.commit()
	
	# Print to console for testing.
	print('update_floor')
	
	# Returns arguments
	message = F'{l_name}, {f_name} - floor number updated to: {new_data}'
	return message
	
def update_warden_zone(l_name, f_name, new_data):
	
	# Execute SQL
	cursor.execute('''UPDATE staff SET mobility_assistance = ? WHERE last_name = ? AND first_name = ?'''\
	,(new_data, l_name, f_name,))
	
	# Commit changes to database
	db.commit()
	
	# Print to console for testing.
	print('update_warden_zone')
	
	# Returns arguments
	message = F'{l_name}, {f_name} - warden zone updated to: {new_data}'
	return message
	
def update_mobility_assistance(l_name, f_name, new_data):

		# Execute SQL
		cursor.execute('''UPDATE staff SET medical_needs = ? WHERE last_name = ? AND first_name = ?'''\
		,(new_data, l_name, f_name,))
		
		# Commit changes to database
		db.commit()
		
		# Print to console for testing.
		print('update_mobility_assistance')
		
		# Returns arguments
		message = F'{l_name}, {f_name} - mobility assistance updated to: {new_data}'
		return message
	
def update_medical_needs(l_name, f_name, new_data):
	
		# Execute SQL
		cursor.execute('''UPDATE staff SET medical_needs = ? WHERE last_name = ? AND first_name = ?'''\
		,(new_data, l_name, f_name,))
		
		# Commit changes to database
		db.commit()
		
		# Print to console for testing.
		print('update_medical_needs')
		
		# Returns arguments
		message = F'{l_name}, {f_name} - medical needs updated to: {new_data}'
		return message
	
def create_sorted_document():

	# execute select query
	cursor.execute('''SELECT staff_id, last_name, first_name, floor, warden_zone, mobility_assistance, medical_needs FROM staff\
	ORDER BY last_name''')
	
	# pass fetchall (rows) method to var: all_rows
	all_rows = cursor.fetchall()
	
	with open("sorted_list.txt", "w+") as file: # create/overwrite text file
		# iterate through every row
		for row in all_rows:
			file.write(f' {row[1]}, {row[2]}. Floor: {row[3]}. Warden Zone: {row[4]}. Assistance? {row[5]}. Meds? {row[6]}')
			file.write("\n")
			
	file.close()
	
	messagebox.showinfo("File Operation", "'sorted_list.txt' created or updated.")
	
	# Print to console for testing.
	print('create_sorted_document')
	
def delete_by_id(staff_id):
	cursor.execute('''DELETE FROM staff WHERE staff_id = ? ''', (staff_id,))
	
	# Print to console for testing.
	print('delete_by_id')
	
def show_basic_info():
	print('')
	print('Show Basic Data')
	
def confirm_entry():
	print('')
	print('Confirm')
	
def menu_create_entry():
	print('')
	print('Create Entry')

# Rebuild these as object methods
"""
def fetch_data_confim():

	global fetched_data
	global target_var
	global last_name
	
	#fetched_data = entry_1.get()
	target_var = entry_1.get()
	
	message_display.config(state = 'normal')
	message_display.delete('1.0', END)
	#message_display.insert('1.0', pre_message + fetched_data)
	message_display.insert('1.0', pre_message + target_var)
	entry_1.delete('0', END) # entry widget uses different index reference than text widget!
	
	# Default state of message_display should be disabled after function completes.
	message_display.config(state = 'disabled') # disables application message area to prevent sending unwanted random input
	
	# Print to console for testing.
	print('Calling fetch_data_confim')
	
	
def menu_create_entry():
	
	# Print to console for testing.
	print('menu_create_entry')
	
	# set target variable to be affected when fetch_data_confim is fired by confirm button.
	
	display_numeric()
	
	
	pre_message = "Last name:  "
	message_display.config(state = 'normal') # enables outputting to Application Message area
	message_display.insert(0.0, "Creating new a record.\n\nPlease enter the last name of the staff member below and confirm.")

	
	def get_last_name():
		
		global target_var
		global pre_message
		
		
		target_var = last_name
		pre_message = 'Last name: '
		
		
			
		message_display.config(state = 'normal')
		message_display.insert(0.0, "Please enter the last name for new record and confirm.")
		message_display.config(state = 'disabled')

	get_last_name()
	
"""
	
	
	
	
# new_item_x represents cascading sub-menu
new_item_1 = Menu(menu, tearoff=0) # add first menu category
# add and config menu items for File
new_item_1.add_command(label='Create Staff List (text file)', command=create_sorted_document)	
new_item_1.add_command(label='Exit', command=client_exit) 

menu.add_cascade(label='File', menu=new_item_1) # add top level (File) to first menu category

# create and configure menu items for Display Records
new_item_2 = Menu(menu, tearoff=0) # add second menu category
new_item_2.add_command(label='Display by Entry Number', command=display_numeric)
new_item_2.add_separator()
new_item_2.add_command(label='Display by Last Name', command=display_alphabetic)

menu.add_cascade(label='Display Records', menu=new_item_2) # add top level (Display Records) to first menu category

# and so on...
new_item_3 = Menu(menu, tearoff=0)
new_item_3.add_command(label='Create New Record', command=menu_create_entry)
new_item_3.add_separator()
new_item_3.add_command(label='Modify Record')
new_item_3.add_separator()
new_item_3.add_command(label='Delete Record')

menu.add_cascade(label='Edit Database', menu=new_item_3)

# ROW number TBD:

# Temporarily comment out to de-clutter interface building
"""
# add 'confirm' button related to entry_1
confirm_button = Button(window, text="Confirm", bg="green", fg="white", command=confirm_entry)
confirm_button.grid(row=2, column=2, padx=10)
	
info_button = Button(window, text="Show basic info", command=show_basic_info)
info_button.grid(row=2, column=3, padx=5)
"""

# Functions below are not required every time script is run, and slows it down.
"""	
create_staff_table()
insert_test_data()
"""


# Testing functions

print(current_data.last_name)

# run main loop - last function before closing db
window.mainloop()

db.close()
