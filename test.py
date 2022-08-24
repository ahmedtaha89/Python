
# -------------------------------
# Information About File
# License
# Who Created The File
# When The File Created
# Why The File Created
# Write Beside The Programming Line
# Write Before The Programming Line
# Prevent Code From Run
# -------------------------------

# This is Comment
print("I Love Python")  # This is Inline Comment
print("Programming")  # I Used This Method Because of Bla Bla Bla
print("Programming")  # If You Used Test Method Will Through Error


#this is not comment 
"""
This is
Not
Multiple
Line
Comments
"""

# ----------------------------
# type()
# All Data in Python is Object
# ----------------------------

print(type(10))  # int => Integer
print(type(100))  # int => Integer
print(type(-50))  # int => Integer

print(type(100.9))  # float => Floating Point Number
print(type(1.0950950))  # float => Floating Point Number
print(type(-100.9595))  # float => Floating Point Number

print(type("Hello Python"))  # str => String

print(type([1, 2, 3, 4, 5]))  # list => List

print(type((1, 2, 3, 4, 5)))  # tuple => Tuple

print(type({"One": 1, "Two": 2, "Three": 3}))  # dict => Dictionary

print(type(2 == 20))  # bool => Boolean


# --------------------------------------
# -- Variables --
# ---------------
# Syntax => [Variable Name] [Assignment Operator] [Value]
#
# Name Convention and Rules
# [1] Can Start With (a-z A-Z) Or Underscore
# [2] You Cannot With Num Or Special Characters
# [3] Can Include (0-9) Or Underscore
# [4] Cannot Include Special Characters
# [5] Name is Not Like name [ Case Sensitive ]
# --------------------------------------

name = "Osama Elzero"  # Single Word => Normal
myName = "Osama Elzero"  # Two Words => camelCase
my_name = "Osama Elzero"  # Two Words => snake_case

print(name)
print(myName)
print(my_name)

#variable
x = 5
y = "test"
z = 4

print(x)
print(y)
print(z)
print(x+z)

x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)




#Camel Case
#Each word, except the first, starts with a capital letter:
#myVariableName = "John"

#Pascal Case
#Each word starts with a capital letter:
#MyVariableName = "John"

#Snake Case
#Each word is separated by an underscore character:
#my_variable_name = "John"


#Many Values to Multiple Variables
#Python allows you to assign values to multiple variables in one line:
#Example
#x, y, z = "Orange", "Banana", "Cherry"

#print(x)
#print(y)
#print(z)


x = "Python "
y = "is "
z = "awesome"
print(x , y ,z)

f = 0


f="guru"

print(f + str(99))

# Declare a variable and initialize it
f = 101
print (f)
# Global vs. local variables in functions
def someFunction():
# global f
    f = 'I am learning Python'
    print (f)
someFunction()
print (f)


help("keywords")