#!/usr/bin/python
# tut 13
print """
Video 13=================
"""

from testing import *

my_duosmart_function(45, 200, "multiply")
def function_two():
	print("you dun fucked up!")

function_two()

# tut 14
print """
Video 14=================
"""

class Person:
    
	def __init__(self, name, hair_color, height):
		self.name = name
		self.hair_color = hair_color
		self.height = height

	def print_name(self, another_value):
		print(self.name + another_value)

	def print_height(self):
		print(self.hair_color)

	def print_hair_color(self):
		print(self.height)

# tut 15
print """
Video 15=================
"""

class Employee(Person):
	def __init__(self, name, hair_color, height, employee_id):
		Person.__init__(self, name, hair_color, height)
		self.employee_id = employee_id

	def print_employee_id(self):
		print(self.employee_id)

employee_one = Employee("spencer", "blonde", "5-9", "a123")
employee_one.print_employee_id()
employee_one.print_hair_color()
employee_one.print_height()
employee_one.print_name()
