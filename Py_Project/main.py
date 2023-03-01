# import my_mod
# my_mod.say_hello("ahmed")
# my_mod.say_welcome("ahmed")

# from my_mod import say_welcome
# say_welcome("taha")

# from my_mod import say_welcome as new_welcome 
# new_welcome("abo taha")
# -----------------------------------
# -- Date and Time => Introduction --
# -----------------------------------

import datetime

# print(dir(datetime))
# print(dir(datetime.datetime))

# Print The Current Date and Time
print(datetime.datetime.now())

# print("#" * 40)

# # Print The Current Year
# print(datetime.datetime.now().year)

# # Print The Current Month
# print(datetime.datetime.now().month)

# # Print The Current Day
# print(datetime.datetime.now().day)

# print("#" * 40)

# # Print Start and End Of Date
# print(datetime.datetime.min)
# print(datetime.datetime.max)

# print("#" * 40)

# # print(dir(datetime.datetime.now()))

# # Print The Current Time
# print(datetime.datetime.now().time())

# print("#" * 40)

# # Print The Current Time Hour
# print(datetime.datetime.now().time().hour)

# # Print The Current Time Minute
# print(datetime.datetime.now().time().minute)

# # Print The Current Time Second
# print(datetime.datetime.now().time().second)

# print("#" * 40)

# # Print Start and End Of Time
# print(datetime.time.min)
# print(datetime.time.max)

# print("#" * 40)

# # Print Specific Date
# print(datetime.datetime(1982, 10, 25))
# print(datetime.datetime(1982, 10, 25, 10, 45, 55, 150364))

# print("#" * 40)

# myBirthDay = datetime.datetime(1982, 10, 25)
# dateNow = datetime.datetime.now()

# print(f"My Birthday is {myBirthDay} And ", end="")
# print(f"Date Now Is {dateNow}")

# print(f" I Lived For {dateNow - myBirthDay}")
# print(f" I Lived For {(dateNow - myBirthDay).days} Days.")


# The Date Is "2021, 6, 25"
# Today Is "2021, 8, 10"

# Message Will Be
# "Days From 2021-06-25 To 2021-08-10 Is => 46"

import datetime
date = datetime.datetime(2021,6,25)
Today = datetime.datetime.now()
print(f"Days From {date} To {Today}Is => {(Today-date).days}")
# Today Is "2021, 8, 10"

# "2021-08-10"
# "Aug 10, 2021"
# "10 - Aug - 2021"
# "10 / Aug / 21"
# "10 / August / 2021"
# "Tue, 10 August 2021"

d =datetime.datetime(2021,8,10)

# "Aug 10, 2021"
print(f"{d.strftime('%b ' ' %d' ' %y' ) }")

# "10 - Aug - 2021"
print(d.strftime("%d - %b - %Y") )

# "10 / Aug / 21"
print(d.strftime("%d - %b - %y") )

# "10 / August / 2021"
print(d.strftime("%d - %B - %Y") )

# "Tue, 10 August 2021"
print(d.strftime("%a %d - %B - %Y") )

# --------------------------
# -- Iterable vs Iterator --
# --------------------------
# Iterable
# [1] Object Contains Data That Can Be Iterated Upon
# [2] Examples (String, List, Set, Tuple, Dictionary)
# ------------------------------------------
# Iterator
# [1] Object Used To Iterate Over Iterable Using next() Method Return 1 Element At A Time
# [2] You Can Generate Iterator From Iterable When Using iter() Method
# [3] For Loop Already Calls iter() Method on The Iterable Behind The Scene
# [4] Gives "StopIteration" If Theres No Next Element
# -----------------------------------------------------------

# myString = "Osama"

# myList = [1, 2, 3, 4, 5]

# for letter in myString:

#   print(letter, end=" ")

# for number in myList:

#   print(number, end=" ")


# for letter in iter("Elzero"):

#   print(letter, end=" ")

# for  text in "ahmed":
#     print(text,end=" - ")

myString = "Osama"    
myIterator = iter(myString)

print(next(myIterator),end=" ")
print(next(myIterator),end=" ")
# print(next(myIterator))
# print(next(myIterator))
# print(next(myIterator))

def reverse_string(my_string):
 yield reversed(my_string)
 

for c in reverse_string("Elzero"):
  print(c)