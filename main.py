# GUI build of staff emergency database application

import sqlite3
from tkinter import *
from tkinter import scrolledtext
from tkinter import Menu

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

# File --> Exit
def client_exit():
	exit()


# Tkinter widgets
window = Tk()
window.title("Database Manager: CPM staff emergency information")
window.geometry('800x600')

# create menu object
menu = Menu(window)


new_item_1 = Menu(menu)

# label button and wire function to it
new_item_1.add_command(label='Exit', command=client_exit)

# pin exit_button to File menu on file bar
menu.add_cascade(label='File', menu=new_item_1)

new_item_2 = Menu(menu)
new_item_2.add_command(label='Button 2')
new_item_2.add_separator()
new_item_2.add_command(label='Button 3')
menu.add_cascade(label='More Buttons', menu=new_item_2)


# main text area (scrollable)
text_1 = scrolledtext.ScrolledText(window,width=95,height=25)
text_1.grid(column=0,row=0)

# pin the menu widget to the window object
window.config(menu=menu)



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
		print('Tried to create staff table, but it already exists.')	

def insert_data(last_name, first_name, floor, warden_zone, mob_ass, med_needs):
# insert dest data into staff table

	# insert info into staff table
	cursor.execute('''INSERT INTO staff(last_name, first_name, floor, warden_zone, mobility_assistance, medical_needs)
					VALUES(?,?,?,?,?,?)''',(last_name, first_name, floor, warden_zone, mob_ass, med_needs))
	
	# commit to database
	db.commit()
	
	# Message to user
	print('Data inserted into staff table.')
	
def insert_test_data():
	insert_data("Doe", "Jane", 1, 1, "no", "no")
	insert_data("Spade", "Sam", 3, 5, "yes", "insulin")
	insert_data("Gomez", "Sal", 2, 3, "no", "no")
	insert_data("Washington", "Kaylee", 2, 3, "yes", "wheelchair")
	insert_data("Chang", "Sarah", 3, 6, "no", "no")
	insert_data("Jennings", "Robert", 1, 2, "yes", "cast (arm)")
	insert_data("Goldsmith", "Chloe", 2, 4, "no", "no")
	insert_data("Brown", "Marvin", 2, 5, "no", "no")
	
def update_test_data():

	statement = '''
	UPDATE staff
	SET mobility_assistance = 'yes'
	WHERE last_name = 'Gomez' AND first_name = 'Sal'
	'''
	
	cursor.execute(statement)
	db.commit()
	
def update_floor(l_name, f_name, new_data):
	
	# Execute SQL
	cursor.execute('''UPDATE staff SET floor = ? WHERE last_name = ? AND first_name = ?'''\
	,(new_data, l_name, f_name,))
	
	# Commit changes to database
	db.commit()
	
	print('')
	
	# Returns arguments
	message = F'{l_name}, {f_name} - floor number updated to: {new_data}'
	return message
	
def update_warden_zone(l_name, f_name, new_data):
	
	# Execute SQL
	cursor.execute('''UPDATE staff SET mobility_assistance = ? WHERE last_name = ? AND first_name = ?'''\
	,(new_data, l_name, f_name,))
	
	# Commit changes to database
	db.commit()
	
	print('')
	
	# Returns arguments
	message = F'{l_name}, {f_name} - warden zone updated to: {new_data}'
	return message
	
def update_mobility_assistance(l_name, f_name, new_data):

		# Execute SQL
		cursor.execute('''UPDATE staff SET medical_needs = ? WHERE last_name = ? AND first_name = ?'''\
		,(new_data, l_name, f_name,))
		
		# Commit changes to database
		db.commit()
		
		print('')
		
		# Returns arguments
		message = F'{l_name}, {f_name} - mobility assistance updated to: {new_data}'
		return message
	
def update_medical_needs(l_name, f_name, new_data):
	
		# Execute SQL
		cursor.execute('''UPDATE staff SET medical_needs = ? WHERE last_name = ? AND first_name = ?'''\
		,(new_data, l_name, f_name,))
		
		# Commit changes to database
		db.commit()
		
		print('')
		
		# Returns arguments
		message = F'{l_name}, {f_name} - medical needs updated to: {new_data}'
		return message
	
def create_sorted_document():

	# execute select query
	cursor.execute('''SELECT staff_id, last_name, first_name, floor, warden_zone, mobility_assistance, medical_needs FROM staff\
	ORDER BY last_name''')
	
	# pass fetchall (rows) method to var: all_rows
	all_rows = cursor.fetchall()
	
	with open("sorted_list.txt", "w+") as file:
		# iterate through every row
		for row in all_rows:
			file.write(f'{row[1]}, {row[2]}. Floor: {row[3]}. Warden Zone: {row[4]}. Assistance? {row[5]}. Meds? {row[6]}')
			file.write("\n")
			
	file.close()
	
def delete_by_id(staff_id):
	cursor.execute('''DELETE FROM staff WHERE staff_id = ? ''', (staff_id,))
		
def display_records(mode):
	
	if (mode == 'numeric'):
		#execute select query, default sort by primary key
		cursor.execute('''SELECT staff_id, last_name, first_name, floor, warden_zone, mobility_assistance, medical_needs FROM staff''')
	elif (mode == 'alphabetic'):
		# execute select query, sort alphabetically by last name
		cursor.execute('''SELECT staff_id, last_name, first_name, floor, warden_zone, mobility_assistance, medical_needs FROM staff\
		ORDER BY last_name''')
		
	# pass fetchall (rows) method to var: all_rows
	all_rows = cursor.fetchall()
	
	# iterate through every row
	for row in all_rows:
		
		if (mode == 'numeric'):
			# display with staff_id leading
			content = f'{row[0]})  {row[1]}, {row[2]} | Floor: {row[3]} | Warden Zone: {row[4]} | Assistance: {row[5]} | Med: {row[6]}'
			text_1.insert(INSERT, content + '\n')
			
		elif (mode == 'alphabetic'):
			# Don't display staff_id
			content = f'{row[1]}, {row[2]} | Floor: {row[3]} | Warden Zone: {row[4]} | Assistance: {row[5]} | Med: {row[6]}'
			text_1.insert(INSERT, content + '\n')
	
	text_1.config(state = 'disabled')
		
		
# create_staff_table()
# insert_test_data()

# display_records('alphabetic')

# create_sorted_document()

# run main loop - last function before closing db
window.mainloop()

db.close()




