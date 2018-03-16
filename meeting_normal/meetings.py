"""
Meeting Manager Module

Authors:
	D.Swaroop Kumar  <somu9042@gmail.com>

"""

from tabulate import tabulate

class MeetingManager:
	"""
	General MeetingManager Class for Scheduling 
	a Meeting With Manager
	"""
	
	def __init__(self):
		"""

		Constructor Function For This Class
		Executed by intrepreter to create a instance of this class

		Attributes:
			self.dict_name --> This Dictionary Will Have Time Slots (str) 
								Stored With indexes as integers For user 
								input Convenience.
			self.dict_name2 --> This Dictionary will Store The Time slots 
								which have been Reserved .
		"""
		self.dict_name={1:"9:00am",2:"10:00am",3:"3:00pm"}
		self.dict_name2={}
		self.timelis=[]

	def time_view(self):
		"""
		This Method is Used for Viewing The Available Slots (not Reserved)
		"""

		print("Available slots:")
		#Loop Through The Dictionary(dict_name) and Print The Available Slots
		#Using List Comprehension.
		a = [[i,value] for i,value in self.dict_name.items()]

		print(tabulate(a,tablefmt="fancy_grid"))
	
	def schedule(self):
		"""
		Schedules a Meeting With Manager 
		"""

		#Takes Name of User
		name=str(input("Enter your name:"))
		#Takes The Slot Number as input from User
		i=int(input("Enter the Slot number you want:"))
		if i in self.dict_name.keys():
			print("Your meeting has been scheduled succesfully")
			# Appends slot number allotted to User with his Name To dict_name2
			self.dict_name2[i]=name
			#Removes The Reserved Slot from Main Dictionary(dict_name)
			self.dict_name.pop(i,"not present")
		else:

			print("Time slot Unavailable") 
	def filled_slots(self):

		print("Filled slots are:\n")
		#Loop Through The Dictionary(dict_name2) and Print Filled Slots
		b= [[i,value] for i,value in self.dict_name2.items()]
		print(tabulate(b,tablefmt="fancy_grid"))



