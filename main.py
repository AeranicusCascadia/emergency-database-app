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

# File --> Exit
def client_exit():
	exit()

# create and define root window
window = Tk()
window.title("Database Manager: CPM staff emergency information")
window.geometry('800x900')

menu = Menu(window) # add menu (automatically goes on top bar in root window

window.config(menu=menu) # attach the menu to root window

# ROW 0:

#main display box
main_display = scrolledtext.ScrolledText(window,width=95,height=15) # create  scroll text box
main_display.grid(row=0, column=0, columnspan=10, padx=5, pady=10, sticky=W) # place scroll text box by grid coordinate
main_display.config(state = 'disabled') # start disabled. enable through appropriate functions

# ROW 1:

# label for message display box
message_display_label = Label(window, text=' Application Messages: ', bg="blue", fg="white", font=("Arial Bold", 9))
message_display_label.grid(row=1, column=0, columnspan=2, padx=10, pady=15, sticky=W)
	
# ROW 2:

# message display box
message_display = Text(window, width=95, height=3)
message_display.grid(row=2, column=0, columnspan=9, padx=10, pady=10, sticky=W)
message_display.config(state = 'disabled')

# ROW 3:

# label for new entry fields
new_entry_label = Label(window, text=' Fields for entry information: ', bg="blue", fg="white", font=("Arial Bold", 9))
new_entry_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky=W)

# ROW 4:

# last name field label
field_last_name_label = Label(window, text='Last Name: ', bg="white", fg="blue", font=("Arial Bold", 9))
field_last_name_label.grid(row=4, column=0, padx=10, sticky=W)

# last name field entry
field_last_name = Entry(window, width=25)
field_last_name.grid(row=4, column=1, pady=15, sticky=W)
field_last_name.config(state = 'disabled')

# first name field label
field_first_name_label = Label(window, text='First Name: ', bg="white", fg="blue", font=("Arial Bold", 9))
field_first_name_label.grid(row=4, column=2, padx=5, ipadx=5)

# first name field entry
field_first_name = Entry(window, width=25)
field_first_name.grid(row=4, column=3, sticky=W)
field_first_name.config(state = 'disabled')

# ROW 5:

# floor field label
field_floor_label = Label(window, text='Floor: ', bg="white", fg="blue", font=("Arial Bold", 9))
field_floor_label.grid(row=5, column=0, padx=10, sticky=W)

# floor field entry
field_floor = Entry(window, width=25)
field_floor.grid(row=5, column=1, pady=10, sticky=W)
field_floor.config(state = 'disabled')

# warden zone field label
field_warden_zone_label = Label(window, text='Warden Zone: ', bg="white", fg="blue", font=("Arial Bold", 9))
field_warden_zone_label.grid(row=5, column=2, padx=5)

# warden zone field entry
field_warden_zone = Entry(window, width=25)
field_warden_zone.grid(row=5, column=3, pady=10, sticky=W)
field_warden_zone.config(state = 'disabled')

# ROW 6:

# mobility assistance field label
mobility_assistance_label = Label(window, text='Mobility Assistance: ', bg="white", fg="blue", font=("Arial Bold", 9))
mobility_assistance_label.grid(row=6, column=0, padx=10, sticky=W)

# mobility assistance field entry
field_mobility_assistance = Entry(window, width=25)
field_mobility_assistance.grid(row=6, column=1, pady=10, sticky=W)
field_mobility_assistance.config(state = 'disabled')

# medical needs field label
field_medical_needs_label = Label(window, text='Medical Needs: ', bg="white", fg="blue", font=("Arial Bold", 9))
field_medical_needs_label.grid(row=6, column=2, padx=5)

# medical needs field entry
field_medical_needs = Entry(window, width=25)
field_medical_needs.grid(row=6, column=3, pady=10, sticky=W)
field_medical_needs.config(state = 'disabled')
	
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
		

# class to handle application data
class DataObject:
	
	# constructor
	def __init__(self, submit_entry_flag, delete_flag, last_name, first_name, floor, warden_zone, mob_ass, med_needs):
	
		self.submit_entry_flag = submit_entry_flag
		self.delete_flag = delete_flag
		self.last_name = last_name
		self.first_name = first_name
		self.floor = floor
		self.warden_zone = warden_zone
		self.mob_ass = mob_ass
		self.med_needs = med_needs
		
	def set_last_name(self):
		self.last_name = field_last_name.get()
		
	def set_first_name(self):
		self.first_name = field_first_name.get()
		
	def set_floor(self):
		self.floor = field_floor.get()
		
	def set_warden_zone(self):
		self.warden_zone = field_warden_zone.get()
		
	def set_mobility_assistance(self):
		self.mob_ass = field_mobility_assistance.get()
		
	def set_medical_needs(self):
		self.med_needs = field_medical_needs.get()
		
	def insert_data(self):
		# insert info into staff table
		cursor.execute('''INSERT INTO staff(last_name, first_name, floor, warden_zone, mobility_assistance, medical_needs)
					VALUES(?,?,?,?,?,?)''',(self.last_name, self.first_name, self.floor, \
					self.warden_zone, self.mob_ass, self.med_needs))
		
		# commit to database
		db.commit()
		
	def delete_data(self):
	
		
		cursor.execute('''DELETE FROM staff WHERE last_name = ? AND first_name = ?''', (self.last_name, self.first_name))
		
		# commit to database
		db.commit()
			
		# Update message to user
		message = F"Attempting to delete entry for {current_data.last_name}, {current_data.first_name}. Updated records are displayed above."
		message_display.config(state = 'normal')
		message_display.delete(1.0, END)
		message_display.insert(END, message)
		message_display.config(state = 'disabled')
		
		"""
		message = F"Unable to delete entry: {self.last_name}, {self.first_name}."
		message_display.config(state = 'normal')
		message_display.delete(1.0, END)
		message_display.insert(END, message)
		message_display.config(state = 'disabled')
		"""
		
	def set_all_data(self):
	
		self.set_last_name()
		self.set_first_name()
		self.set_floor()
		self.set_warden_zone()
		self.set_mobility_assistance()
		self.set_medical_needs()
		
	def reset_data_defaults(self):
	
		self.submit_entry_flag = False
		self.delete_flag = False
		self.last_name = 'default last name'
		self.first_name = 'default first name'
		self.floor = 0
		self.warden_zone = 0
		self.mob_ass = 'no'
		self.med_needs = 'no'
		
		
# Our sole instance of DataObject class
current_data = DataObject(False, False, 'default last name', 'default first name', 0, 0, 'no', 'no')


def clear_and_disable_fields():
	
	# clear and disable entry fields
	field_last_name.delete(0, END)
	field_last_name.config(state = 'disabled')
	field_first_name.delete(0, END)
	field_first_name.config(state = 'disabled')
	field_floor.delete(0, END)
	field_floor.config(state = 'disabled')
	field_warden_zone.delete(0, END)
	field_warden_zone.config(state = 'disabled')
	field_mobility_assistance.delete(0, END)
	field_mobility_assistance.config(state = 'disabled')
	field_medical_needs.delete(0, END)
	field_medical_needs.config(state = 'disabled')


def submit_entry_button_method():
	
	# check submit entry flag enabled
	if (current_data.submit_entry_flag == True):
	
		print('')
		print('Fetch from fields enabled.')
		
		"""
		# fetching methods
		current_data.set_last_name()
		current_data.set_first_name()
		current_data.set_floor()
		current_data.set_warden_zone()
		current_data.set_mobility_assistance()
		current_data.set_medical_needs()
		"""
		
		# call main setter method
		current_data.set_all_data()
		
		# Print to console for testing
		print('')
		print(current_data.last_name + ', ' + current_data.first_name)
		print(F'Floor: {current_data.floor}, Warden Zone: {current_data.warden_zone}')
		print(F'Mobility Assistance: {current_data.mob_ass}')
		print(F'Medical Needs: {current_data.med_needs}')
		
		# call data insertion method
		current_data.insert_data()
		
		clear_and_disable_fields()
		
		# moved all this into a function, which is called above.
		# remove the following after testing
		"""
		# clear and disable entry fields
		field_last_name.delete(0, END)
		field_last_name.config(state = 'disabled')
		field_first_name.delete(0, END)
		field_first_name.config(state = 'disabled')
		field_floor.delete(0, END)
		field_floor.config(state = 'disabled')
		field_warden_zone.delete(0, END)
		field_warden_zone.config(state = 'disabled')
		field_mobility_assistance.delete(0, END)
		field_mobility_assistance.config(state = 'disabled')
		field_medical_needs.delete(0, END)
		field_medical_needs.config(state = 'disabled')
		"""
		
		# update message to user
		message_display.config(state = 'normal')
		message_display.delete(1.0, END)
		
		message = F'New entry for {current_data.last_name}, {current_data.first_name} created.'
		message_display.insert(END, message)
		message_display.config(state = 'disabled')
		
		# Refresh display of records
		display_alphabetic()
		
		# Reset submit entry flag back to false
		current_data.submit_entry_flag = False
		
		# reset data
		current_data.reset_data_defaults()
		
	else:
		print('')
		print('Submit Entry flag is still disabled.')
		
		message = "Please select 'Create New Record' from the 'Edit Database' menu in the menu bar to begin\ncreating a new staff record entry."
		
		message_display.config(state = 'normal')
		message_display.delete(1.0, END)
		message_display.insert(END, message)
		message_display.config(state = 'disabled')
	
def delete_entry_button_method():
	if (current_data.delete_flag == True):
		
		# setters
		current_data.set_last_name()
		current_data.set_first_name()
		
		# call delete method
		current_data.delete_data()
		
		
		# Refresh display of records
		display_alphabetic()
		
		# reset data
		current_data.reset_data_defaults()
		
		# reset delete flag to false
		current_data.delete_flag = False
			
	else:
		print('Delete flag still set to False')
	
		message = "Select the 'Delete Record' option from the 'Edit Database' menu in the menu bar."
		message_display.config(state = 'normal')
		message_display.delete(1.0, END)
		message_display.insert(END, message)
		message_display.config(state = 'disabled')
	
	# clear and disable name entry fields
	field_last_name.delete(0, END)
	field_first_name.delete(0, END)
	field_last_name.config(state = 'disabled')
	field_first_name.config(state = 'disabled')
	
# Modify entry function goes here


def cancel_action_button_method():
	
	# reset data
	current_data.reset_data_defaults()
	
	# clear and disable text entry fields
	clear_and_disable_fields()
	
	# Message to user
	message = "Current action cancelled."
	message_display.config(state = 'normal')
	message_display.delete(1.0, END)
	message_display.insert(END, message)
	message_display.config(state = 'disabled')



def menu_delete_entry():

	# Toggle delete flag to set behavior or Delete Entry button method
	current_data.delete_flag = True
	
	# Message to user
	message = "Please enter the last and first names for the entry you wish to delete in the fields below,\nthen press the 'Delete Entry' button."
	message_display.config(state = 'normal')
	message_display.delete(1.0, END)
	message_display.insert(END, message)
	message_display.config(state = 'disabled')
	
	# enable last and first name fields
	field_last_name.config(state = 'normal')
	field_first_name.config(state = 'normal')
	
def menu_create_entry():

	# set fetch flag to True
	current_data.submit_entry_flag = True

	print('')
	print('Create Entry')
	
	"""
	main_display.config(state = 'normal')
	main_display.delete(1.0, END)
	main_display.config(state = 'disabled')
	"""
	
	message_display.config(state = 'normal')
	field_last_name.config(state = 'normal')
	field_first_name.config(state = 'normal')
	field_floor.config(state = 'normal')
	field_warden_zone.config(state = 'normal')
	field_mobility_assistance.config(state = 'normal')
	field_medical_needs.config(state = 'normal')
	
	message = "Please fill in the fields below, then click the 'Submit' button to create a new entry."
	
	message_display.delete(1.0, END)
	message_display.insert(END, message)
	message_display.config(state = 'disabled')
	
	
		
	"""
	main_display
	message_display
	field_last_name
	field_first_name
	field_floor
	field_warden_zone
	field_mobility_assistance
	field_medical_needs
	"""

# Menu bar	
	
# new_item_x represents cascading sub-menu
new_item_1 = Menu(menu, tearoff=0) # add first menu category
# add and config menu items for File
new_item_1.add_command(label='Create Staff List (text file)', command=create_sorted_document)	
new_item_1.add_command(label='Exit', command=client_exit) 

menu.add_cascade(label='File', menu=new_item_1) # add top level (File) to first menu category

# create and configure menu items for Display Records
new_item_2 = Menu(menu, tearoff=0) # add second menu category
new_item_2.add_command(label='Display by Last Name', command=display_alphabetic)
new_item_2.add_separator()
new_item_2.add_command(label='Display by Entry Number', command=display_numeric)

menu.add_cascade(label='Display Records', menu=new_item_2) # add top level (Display Records) to first menu category

# and so on...
new_item_3 = Menu(menu, tearoff=0)
new_item_3.add_command(label='Create New Record', command=menu_create_entry)
new_item_3.add_separator()
new_item_3.add_command(label='Modify Record')
new_item_3.add_separator()
new_item_3.add_command(label='Delete Record', command=menu_delete_entry)

menu.add_cascade(label='Edit Database', menu=new_item_3)

# ROW 7:

# Submit button
submit_new_button = Button(window, text='Submit New Entry', bg="green", fg="white", font=("Arial Bold", 9), command=submit_entry_button_method)
submit_new_button.grid(row=7, column=0, padx=20, pady=15, ipadx=10, sticky=W)

# Submit modification button
submit_mod_button = Button(window, text='Submit Modification', bg="green", fg="white", font=("Arial Bold", 9))
submit_mod_button.grid(row=7, column=1, padx=20, pady=15, ipadx=10, sticky=W)

# Delete entry button
delete_button = Button(window, text='Delete Entry', bg="red", fg="white", font=("Arial Bold", 9), command=delete_entry_button_method)
delete_button.grid(row=7, column=2, padx=20, pady=15, ipadx=10, sticky=W)

# Delete entry button
cancel_button = Button(window, text='Cancel Action', bg="yellow", fg="red", font=("Arial Bold", 9), command=cancel_action_button_method)
cancel_button.grid(row=7, column=3, padx=20, pady=15, ipadx=10, sticky=W)

# Functions below are not required every time script is run, and slows it down.
"""
create_staff_table()
insert_test_data()
"""

display_alphabetic()


# run main loop - last function before closing db
window.mainloop()

db.close()
