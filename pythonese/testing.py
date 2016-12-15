#!/usr/bin/python

# tut 7
print """
Video 7===============
"""

my_name = "spencer"

if my_name == "spencer":
	print("hi " + my_name)
elif my_name == "billy":
	print("fuck you dude!")
else: 
	print("I don't know you!")
# +++++++++++++++++++++++++++++++++++++++++++

# tut 8 
print """
Video 8================
"""

my_string = "stringity string"
print(my_string[5])

for x in my_string:
	if x == "g":
		print("it's a G!")

fruits = ["banana", "apple", "pear"]

for f in fruits:
	if f == "banana":
		print(" I <3 " + f)
		break

#+++++++++++++++++++++++++++++++++++++++++++++

# tut 9
print """
Video 9=================
"""

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for x in range(1, 6):
	print(x)

#+++++++++++++++++++++++++++++++++++++++++++++

# tut 10
print """
Video 10=================
"""
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

start_number = 0
while start_number < 5:
	print(my_list[start_number])
	start_number += 1

# this will always continually repeat
#while 0 != 1:
#	print("fuck")
    
# tut 12
print """
Video 12=================
"""
def my_function(first_number, second_number):
	print(first_number + second_number)

def my_smart_function(first_number, second_number, math_operation):
	if math_operation == "add":
		print(first_number + second_number)
	elif math_operation == "multiply":
		print(first_number * second_number)
	elif math_operation == "divide":
		print(first_number / second_number)
	else:
		print("done!")

my_smart_function(5, 25, "divide")

# tut 13
print """
Video 13=================
"""

def my_duosmart_function(first_number, second_number, math_operation):
    if math_operation == "add":
        print(first_number + second_number)
    elif math_operation == "multiply":
        print(first_number * second_number)

def function_two():
	print("another one!")
