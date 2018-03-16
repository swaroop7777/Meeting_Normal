"""
Meeting Manager Application Script

Authors:
	D.Swaroop Kumar <somu9042@gmail.com>


**Modules**
	tabulate: The module provides just one function, tabulate, which takes a
			 list of lists or another tabular data type as the first argument,
			 and outputs a nicely formatted plain-text table.

"""

from meetings import MeetingManager
from tabulate import tabulate
import os

# Creating an object of MeetingManager class 
manager = MeetingManager() 

# Application Loop
while True:
	print(tabulate([(1, "View Available TimeSlots",), (2, "Schedule a Meeting"
		,),(3,"See Scheduled Slots")], tablefmt="fancy_grid"))
	print("Hey! Prefer To Choose '1' To See The TimeSlots Before Scheduling")
	ch=int(input("enter your choice:\n"))
	if ch == 1:
		"""
		If user enters 1(int) as input then it 
		Calls the function Present in MeetingManager Class
		called 'timeview()'.
		"""
		os.system('cls')
		manager.time_view()

	elif ch == 2:
		"""
		If user enters 2(int) as input then it 
		Calls the function Present in MeetingManager Class
		called 'schedule()'.
		"""
		os.system('cls')	
		manager.schedule()
	elif ch == 3:
		"""
		If user enters 3(int) as input then it 
		Calls the function Present in MeetingManager Class
		called 'filled_slots()'.
		"""
		os.system('cls')
		manager.filled_slots()

	else:
		print("select valid option!\n")
