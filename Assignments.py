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
Name     = "Ahmed Taha"
Age      = "20"
Country  = "Egypt"

#------------------------------------------------------------------------------------------#

# تكليف 03  
print(" Name: "  + Name  )
print("Age: "       + Age)
print("Country: "   +Country)

#------------------------------------------------------------------------------------------#

# تكليف 04  
print("Hello, My 'Name Is "+ Name +  " And Iam " +Age+ " Years Old and I Live in "+Country+  ".")

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

#"Hello 'Osama', How You Doing \ """ Your Age Is "38"" + And Your Country Is: Egypt

print("\"Hello \'{:s}\' , How You Doing \\   \"\"\" Your Age Is \"{:d}\"\" + And Your Country Is: {:s}" .format(Name,Age,Country)) 
print(f"\"Hello \'{Name}\' , How You Doing \\   \"\"\" Your Age Is \"{Age}\"\" + And Your Country Is: {Country}" )

 #------------------------------------------------------------------------------------------#

 # التكليف 02
print(f"\"Hello \'{Name}\' , How You Doing \\ \n\"\"\" Your Age Is \"{Age}\"\" + \nAnd Your Country Is: {Country}" ) 


#------------------------------------------------------------------------------------------#

 # التكليف 03
 
name = 'Elzero'

# Needed Output
# Second Letter Is "l"
# Third Letter Is "z"
# Last Letter Is "o"
name = 'Elzero'
print("Second Letter Is " + name[1] + "\n" + "Third Letter Is  "  + name[2] +  "\n" + "Last Letter Is " + name[5]) 
print("Second Letter Is " + name[1] + "\n" + "Third Letter Is  "  + name[2] +  "\n" + "Last Letter Is " + name[5]) 

#------------------------------------------------------------------------------------------#

 # التكليف 04
name = 'Elzero'

# Needed Output
# "lze"
# "Ezr"
# "rzE"


print("Second Letter Is " + name[1:4] + "\n" + "Third Letter Is  "  + name[0:5:2] +  "\n" + "Last Letter Is " + name[  6 : 0 : -1]) 

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

# Complex => (Real + imaginary) => 1+2J
a = 1+2J 
print(a.real) 
print(a.imag)



num = 10 
print("%.10f"  %num)