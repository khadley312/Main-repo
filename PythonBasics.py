#!/usr/bin/python


# blocks of code dont use braces, just indentation
print("Hello World")

# used to single line comment
"""
multi line comment
line 2
line 3
line 4
"""

# variables
name = "Keith"
# number
num1 = 5
num2 = 10
print(num1 + num2)
num3 = 12
num4 = 8  # they can be put on same line with a semi-colon
print(num3 + num4)
# float
decimal = 3.3
# conversion to string
to_string = str(num1)
print(to_string)
# conversion to int/float
to_int = int(to_string)
to_float = float(to_string)
print(to_int)
print(to_float)


# the backslash tells Python to continue reading
wholeName = "Keith" + "Hadley"
# these two print the same
wholeName = "Keith" + \
            "Hadley"
print(wholeName)

# substring
first_name = wholeName[0:5]
last_name = wholeName[5:]
print(first_name)
print(last_name)

# control structures
# if/else/elif
age = 8
if age >= 18:
    print("is an adult")
elif age <= 12:
    print("is a kid")
else:
    print("is not an adult")

# ternary
can_drink = True if age >= 21 else False
print("This person can drink")

# while
while age < 50:
    print("Not old enough")
    age += 1

# Lists

my_cars = ["911", "R8", "Lambo", "Ferrari"]
print(my_cars[0:4])
# change item
my_cars[3] = "McLaren"
print(my_cars[0:4])
# remove from list
del my_cars[0]
# iterate
for item in my_cars:
    print(item)

# Dictionary
my_dict = {'name': "Keith", 'state': "Ohio", 'age': 28}
print(my_dict['name'])
# change
my_dict['name'] = "Lewis"
print(my_dict['name'])
# delete
del my_dict['name']
print(my_dict)
# iterate
for k, v in my_dict.items():
    print(k, "=", v)

#Functions - way to recieve input and output
def the_fn():
    #your code here
    print("hello")
    
#multiple arguements in a function
def add(arg1, arg2):
    return(arg1 + arg2)

#returning multiple values from a function
def square (n1, n2):
    return n1**2,n2**2

the_fn()
result = add(arg2=1,arg1=2)
print(square(1,2))
result1, result2 = square(1,2)
print(result1, result2)