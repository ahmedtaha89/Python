#(Lessons from 01 To 10)

# تكليف 01  
#Introduction And Variables
#comment 
#Data Type
#Variables
#escape space
# => \    escape newline and escape backspace
# => \\   escape backspace
# => \n   newline
# => \b   backspace
# => \t   tap
# => \'   escape single quote
# => \"   escape double quote
# => \r   current return
# => \xhh  hex value

#------------------------------------------------------------------------------------------#

# تكليف 02  

from dataclasses import replace
from typing import Concatenate

from test import List, Tuple


Name     = "Ahmed Taha"
Age      = "20"
Country  = "Egypt"

#------------------------------------------------------------------------------------------#

# تكليف 03  

# Concatenation
print("Name: "      + Name)
print("Age: "       +  Age)
print("Country: "   + Country)

#  old way (Format String)
print("Name: %s   "        %Name)
print("Age:  %s   "         %Age)
print("Country: %s"     %Country)


# New way (Format String)
print("Name: {:s}"      .format(Name))
print("Age: {:s}"      .format(Age))
print("Country: {:s}"   .format(Country))


# New way (Format String) => Js
print(f"Name: {Name}")
print(f"Age: {Age}")
print(f"Country: {Country}")



#------------------------------------------------------------------------------------------#

# تكليف 04  
Name     = "Ahmed Taha"
Age      = "20"
Country  = "Egypt"

# "Hello, My Name Is Osama And Iam 38 Years Old and I Live in Egypt."

# Concatenation
print("Hello, My Name Is "+ Name +  " And Iam " +Age+ " Years Old and I Live in "+Country+  ".")
# New way => JS 
print(f"Hello, My Name Is  {Name} And Iam  {Age} Years Old and I Live in {Country} "".")
# Old way 
print("Hello, My Name Is %s And Iam %s Years Old and I Live in %s." %(Name,Age,Country))
# New way 
print("Hello, My Name Is {:s} And Iam {:s} Years Old and I Live in {:s}." .format(Name,Age,Country))


#------------------------------------------------------------------------------------------#

# تكليف 05  

print(type(Name))
print(type(Age))
print(type(Country))

#------------------------------------------------------------------------------------------#





# Strings And Methods

# (Lessons from 10 To 18)

# تكليف 01 

Name     =  "Ahmed Taha"
Age      =  20
Country  = "Egypt"   

# "Hello 'Osama', How You Doing \ """ Your Age Is "38"" + And Your Country Is: Egypt

print("\"Hello \'{:s}\' , How You Doing \\   \"\"\" Your Age Is \"{:d}\"\" + And Your Country Is: {:s}" .format(Name,Age,Country)) 
print(f"\"Hello \'{Name}\' , How You Doing \\   \"\"\" Your Age Is \"{Age}\"\" + And Your Country Is: {Country}" )
#"Hello 'Osama', How You Doing \ """ Your Age Is "38"" + And Your Country Is: Egypt

 #------------------------------------------------------------------------------------------#

 # التكليف 02
 
print(f"Hello \'{Name}\' , How You Doing \\ \n\"\"\" Your Age Is \"{Age}\"\" + \nAnd Your Country Is: {Country}" ) 


#------------------------------------------------------------------------------------------#

 # التكليف 03
 
name = 'Elzero'

# Needed Output
# Second Letter Is "l"
# Third Letter Is "z"
# Last Letter Is "o"
name = 'Elzero'
print("Second Letter Is " + name[1] + "\n" + "Third Letter Is  "  + name[2] +  "\n" + "Last Letter Is " + name[5]) 

#------------------------------------------------------------------------------------------#

 # التكليف 04
 
name = 'Elzero'

# Needed Output
# "lze"
# "Ezr"
# "rzE"


print("Second Letter Is " + name[1:4] + "\n" + "Third Letter Is  "  + name[0:5:2] +  "\n" + "Last Letter Is " + name[-2::-2]) 

#------------------------------------------------------------------------------------------#

#  التكليف 05

name = "#@#@Elzero#@#@"
# Needed Output
# Elzero

print(name.strip("#@"))
print(name.rstrip("#@"))
print(name.lstrip("#@"))

#------------------------------------------------------------------------------------------#
 
 #  التكليف 06
 
a= "9"
b= "15"
c= "130"
d= "950"
e = "1500"

# Needed Output
# 0009
# 0015
# 0130
# 0950
# 1500

print(a.zfill(4))
print(b.zfill(4))
print(c.zfill(4))
print(d.zfill(4))
print(e.zfill(4))


#------------------------------------------------------------------------------------------#

 #  التكليف 07
 
name_one = "Osama"
name_two = "Osama_Elzero"

print(name_one.rjust(20,"@"))
print(name_two.rjust(20,"@"))
 
 #------------------------------------------------------------------------------------------#
 
 #  التكليف 08
 
name_one = "OSamA"
name_two = "osaMA"

print(name_one.swapcase())
print(name_two.swapcase())

 #------------------------------------------------------------------------------------------#

 #  التكليف 09
 
msg = "I Love Python And Although Love Elzero Web School"
print(msg.count("Love"))

 #------------------------------------------------------------------------------------------#

 #  التكليف 10
 
name = "Elzero"

print(name.index("z"))
print(name.find("z"))


 #------------------------------------------------------------------------------------------#

 #  التكليف 11
 
msg = "I <3 Python And Although <3 Elzero Web School"
print(msg.replace("<3","Love", 1 )) 

 #------------------------------------------------------------------------------------------#

 #  التكليف 12
 
msg = "I <3 Python And Although <3 Elzero Web School"
print(msg.replace("<3","Love" )) 

 #------------------------------------------------------------------------------------------#
 
 #  التكليف 13
 
name = "Ahmed"
age = 20
country = "Egypt"

print(f"My Name Is {name}, And My Age Is {age} , And My Country Is {country}")

 #------------------------------------------------------------------------------------------#
 
 
 
 
 
 
# Numbers & Arithmetic Operators 

# (Lessons from 19 To 20)

# تكليف 01 

#  int
#  Float
#  complex

print(type(100))
print(type(10.0))
print(type(100+8J))

#------------------------------------------------------------------------------------------#

# تكليف 02 

# Complex => (Real + imaginary) => 1+2J
a = 1+2J 
print(a.real) 
print(a.imag)
# print((1+2J).real)
# print((1+2J).imag)

#------------------------------------------------------------------------------------------#

# تكليف 03 

num = 10 
print("%.10f"  %num)
print(f"{num:.10f}")

#------------------------------------------------------------------------------------------#

# تكليف 04 

num = 159.650
print(int(num))
print(type(int(num)))

#------------------------------------------------------------------------------------------#

# تكليف 05 

# 100 - 115 = -15  
# 50 * 30 = 1500
# 21 % 4 = 1
# 110 / 11 = 10
# 97 // 20 = 4


#------------------------------------------------------------------------------------------#




# List & Methods 

# (Lessons from 21 To 23)


# تكليف 01 

Friends   =  ["Ammar", "Kareem", "Islam","Faris","Mohmoud"]
print(Friends[0])
print(Friends[-5])
print(Friends[4])
print(Friends[-1])

#------------------------------------------------------------------------------------------#

# تكليف 02 


friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"] 
print(friends[::2])
print(friends[1::2])

#------------------------------------------------------------------------------------------#

# تكليف 03 

print("\n")

friends = ["Osama","Ahmed","Sayed","Ali","Ali","Mahmoud"] 

print(friends[0:-1])
print(friends[-2::-2])

#------------------------------------------------------------------------------------------#

# تكليف 04 

print("\n")
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
friends[-2:] =["Elzero","Elzero"] 
print(friends)


#------------------------------------------------------------------------------------------#

# تكليف 05 

print("\n")
friends = ["Osama", "Ahmed", "Sayed"]
friends.insert(0,"Nasser")
print(friends)
friends.append("Salem")
print(friends)



#------------------------------------------------------------------------------------------#

# تكليف 06 
print("\n")
friends = ["Nasser", "Osama", "Ahmed", "Sayed", "Salem"]
# friends.pop(0:2)
friends[0:2] = []
print(friends)
print("\n")
friends[-1:] = []
print(friends)

#------------------------------------------------------------------------------------------#

# تكليف 07 

print("\n")
friends = ["Ahmed", "Sayed"]
employees = ["Samah", "Eman"]
school = ["Ramy", "Shady"]
employees = ["Samah", "Eman"]
friends.extend(employees)
friends.extend(school)
print(friends)



#------------------------------------------------------------------------------------------#

# تكليف 08 


friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]
friends.sort()
print(friends)
friends.sort(reverse=True)
print(friends)

print("\n")

#------------------------------------------------------------------------------------------#

# تكليف 9 

friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]
print(len(friends))

#------------------------------------------------------------------------------------------#

# تكليف 10 

technologies = ["Html", "CSS", "JS", "Python", ["Django", "Flask", "Web"]]
print(technologies[4][0])
print(technologies[4][-1])



# Tuples & Methods
# (Lessons from 24 To 25)
# تكليف 01 

Name = "Ahmed",
print(Name)
print(type(Name))

#------------------------------------------------------------------------------------------#

# تكليف 02 

friends = ("Osama", "Ahmed", "Sayed")

# a = list(friends)
# a[0] = "Elzero"
# friends = Tuple(a)
# print(friends)

print(type(friends))
print(len(friends))

#------------------------------------------------------------------------------------------#

# تكليف 03 

nums = (1, 2, 3)
letters = ("A", "B", "C")
Concatenate = nums + letters
print(Concatenate)
print(len(Concatenate))


#------------------------------------------------------------------------------------------#

# تكليف 04 

my_tuple = (1, 2, 3, 4)
a,b,_,c = my_tuple
print(a)
print(b)
print(c)

print("-" * 50 )

#------------------------------------------------------------------------------------------#

# Set, Dictionary & Methods
# (Lessons from 26 To 32)

# تكليف 01 


My_List = [1,2,3,4,5,1]
Unique_List = list(set(My_List))
print(Unique_List)
print(type(Unique_List))
Unique_List.remove(5)
print(Unique_List)

print("-" * 50 )

#------------------------------------------------------------------------------------------#

# تكليف 02 

nums = {1, 2, 3}
letters = {"A", "B", "C"}

print(nums.union(letters))
print(nums  | letters)
nums.update(letters)
print(nums)
print("-" * 50 )

#------------------------------------------------------------------------------------------#

# تكليف 03 

nums = {1, 2, 3}
letters = {"A", "B", "C"}
print(nums)
nums.clear()
print(nums)

print("-" * 50 )

nums.update("A","B")
print(nums)

nums.discard("C")
print(nums)


#------------------------------------------------------------------------------------------#

# تكليف 04 

print("-" * 50 )


set_one = {1, 2, 3}
set_two = {1, 2, 3, 4, 5, 6}

print(set_one.issubset(set_two))


#------------------------------------------------------------------------------------------#

# تكليف 05 

My_Skills = {
    
    "HTML"  : "HTML Progress Is 90%" ,
    "CSS"   : "CSS Progress Is 80%",
    "Python": "Python Progress Is 30%"
}


print(My_Skills["HTML"])
print(My_Skills["CSS"])
print(My_Skills["Python"])




My_Skills["Ai"] = " AI Progress Is 20%"
My_Skills.update({"ai" : "AI Progress Is 20%"})


print(My_Skills)