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
window.geometry('800x830')

menu = Menu(window) # add menu (automatically goes on top bar in root window

window.config(menu=menu) # attach the menu to root window

# ROW 0:

#main display box
main_display = scrolledtext.ScrolledText(window,width=95,height=25) # create scroll text box
main_display.grid(row=0, column=0, columnspan=10, padx=5, pady=10, sticky=W) # place scroll text box by grid coordinate
main_display.config(state = 'disabled') # start disabled. enable through appropriate functions

# ROW 1:

# label for message display box
message_display_label = Label(window, text=' Application Messages: ', bg="blue", fg="white", font=("Arial Bold", 9))
message_display_label.grid(row=1, column=0, columnspan=2, padx=10, pady=15, sticky=W)
	
# ROW 2:

# message display box
message_display = Text(window, width=80, height=5)
message_display.grid(row=2, column=0, columnspan=9, padx=10, pady=10, sticky=W)
message_display.config(state = 'disabled')

# ROW 3:

# label for new entry fields
new_entry_label = Label(window, text=' Fields for entry information: ', bg="blue", fg="white", font=("Arial Bold", 9))
new_entry_label.grid(row=3, column=0, padx=10, columnspan=2, pady=20, sticky=W)

# ROW 4:

# last name field label
field_last_name_label = Label(window, text='Last Name: ', bg="white", fg="blue", font=("Arial Bold", 9))
field_last_name_label.grid(row=4, column=0, padx=10, sticky=W)

# last name field entry
field_last_name = Entry(window, width=32)
field_last_name.grid(row=4, column=1, pady=15, sticky=W)
field_last_name.config(state = 'disabled')

# first name field label
field_first_name_label = Label(window, text='First Name: ', bg="white", fg="blue", font=("Arial Bold", 9))
field_first_name_label.grid(row=4, column=2, padx=10, sticky=W)


# first name field entry
field_first_name = Entry(window, width=32)
field_first_name.grid(row=4, column=3, pady=10, sticky=W)
field_first_name.config(state = 'disabled')

# ROW 5:

# floor field label
field_floor_label = Label(window, text='Floor: ', bg="white", fg="blue", font=("Arial Bold", 9))
field_floor_label.grid(row=5, column=0, padx=10, sticky=W)

# floor field entry
field_floor = Entry(window, width=32)
field_floor.grid(row=5, column=1, pady=10, sticky=W)
field_floor.config(state = 'disabled')

# warden zone field label
field_warden_zone_label = Label(window, text='Warden Zone: ', bg="white", fg="blue", font=("Arial Bold", 9))
field_warden_zone_label.grid(row=5, column=2, padx=10, sticky=W)

# warden zone field entry
field_warden_zone = Entry(window, width=32)
field_warden_zone.grid(row=5, column=3, pady=10, sticky=W)
field_warden_zone.config(state = 'disabled')

# ROW 6:

# mobility assistance field label
mobility_assistance_label = Label(window, text='Mobility Assistance: ', bg="white", fg="blue", font=("Arial Bold", 9))
mobility_assistance_label.grid(row=6, column=0, padx=10, sticky=W)

# mobility assistance field entry
field_mobility_assistance = Entry(window, width=32)
field_mobility_assistance.grid(row=6, column=1, pady=10, sticky=W)
field_mobility_assistance.config(state = 'disabled')

# medical needs field label
field_medical_needs_label = Label(window, text='Medical Needs: ', bg="white", fg="blue", font=("Arial Bold", 9))
field_medical_needs_label.grid(row=6, column=2, padx=10, sticky=W)

# medical needs field entry
field_medical_needs = Entry(window, width=32)
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
	def __init__(self, fetch_flag, last_name, first_name, floor, warden_zone, mob_ass, med_needs):
	
		self.fetch_flag = fetch_flag
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
	
		
# Our sole instance of DataObject class
current_data = DataObject(False, 'default last name', 'default first name', 0, 0, 'no', 'no')

def create_entry_from_fields():
	
	# check fetch flag enabled
	if (current_data.fetch_flag == True):
	
		print('')
		print('Fetch from fields enabled.')
		
		# fetching methods
		current_data.set_last_name()
		current_data.set_first_name()
		current_data.set_floor()
		current_data.set_warden_zone()
		current_data.set_mobility_assistance()
		current_data.set_medical_needs()
		
		# Print to console for testing
		print('')
		print(current_data.last_name + ', ' + current_data.first_name)
		print(F'Floor: {current_data.floor}, Warden Zone: {current_data.warden_zone}')
		print(F'Mobility Assistance: {current_data.mob_ass}')
		print(F'Medical Needs: {current_data.med_needs}')
		
		current_data.insert_data()
	
		
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
		
		
		
	else:
		print('')
		print('Fetch from fields is still disabled.')
	
	
	
def menu_create_entry():

	# set fetch flag to True
	current_data.fetch_flag = True

	print('')
	print('Create Entry')
	
	# enable text field, clear it, then disable it
	main_display.config(state = 'normal')
	main_display.delete(1.0, END)
	main_display.config(state = 'disabled')
	
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
new_item_2.add_command(label='Display by Entry Number', command=display_numeric)
new_item_2.add_separator()
new_item_2.add_command(label='Display by Last Name', command=display_alphabetic)

menu.add_cascade(label='Display Records', menu=new_item_2) # add top level (Display Records) to first menu category

# and so on...
new_item_3 = Menu(menu, tearoff=0)
new_item_3.add_command(label='Create or Modify Record', command=menu_create_entry)
new_item_3.add_separator()
new_item_3.add_command(label='Modify Record')
new_item_3.add_separator()
new_item_3.add_command(label='Delete Record')

menu.add_cascade(label='Edit Database', menu=new_item_3)

# ROW 7:

# Submit button
submit_button = Button(window, text='Create New Entry', bg="green", fg="white", font=("Arial Bold", 10), command=create_entry_from_fields)
submit_button.grid(row=7, column=0, padx=20, pady=15, ipadx=15, sticky=W)
	
# Functions below are not required every time script is run, and slows it down.
"""	
create_staff_table()
insert_test_data()
"""



# run main loop - last function before closing db
window.mainloop()

db.close()
