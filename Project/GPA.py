# Num_Courses = 2
# count = 0
# Points = 0
# while count < Num_Courses:
#  Code = str(input("Enter The Code Of Course: ").lower())
#  Grade = int(input("Enter Your Grade: "))
#  count+=1
#  if Grade < 50:   
#     Points == 0
#  elif  Grade >= 50 and Grade < 60:
#     Points == 1.7 
#  elif  Grade >= 60 and Grade < 65:
#     Points == 2    
#  elif  Grade >= 65 and Grade < 70:
#     Points == 2.4
#  elif  Grade >= 70 and Grade < 75:
#     Points == 2.7
#  elif  Grade >= 75 and Grade < 80:
#     Points == 3
#  elif  Grade >= 80 and Grade < 85 :
#     Points == 3.3                   
#  elif  Grade >= 85 and Grade < 90 :
#     Points == 3.7     
#  elif  Grade >= 90 :
#     Points == 4   

#     print(Points)    




# def function_name():

#   return "Hello Python From Inside Function"

# print(function_name())

# def Age_Calc(age):

#    Age = int(input("Enter Your Age: "))
   # unit = str(input("Please Choose Time Unit: All , Months, Weeks, Days or (m , w , d): ")).strip().lower()

   # Months = Age * 12
   # Weeks = Months * 4
   # Days = Weeks * 365

   # if unit == "months" or unit == "m":
   #    print(f"You Lived For {Months} Months")

   # elif  unit == "weeks" or unit == "w":
   #    print(f"You Lived For {Weeks} Weeks")  

   # elif  unit == "days" or unit == "d":
   #    print(f"You Lived For {Days:,} Days")   

   # elif  unit == "all" or unit == "a":
   #    print(f"You Lived For {Age} Age {Months} Months , {Weeks} Weeks , {Days:,} Days")    
   # print(f"You Lived For {Age} Age {Months} Months , {Weeks} Weeks , {Days:,} Days") 


# Function To Calc Age   
# Age_Calc(20)




# def calc(n1, operator ,  n2):
#    if type(n1) != int and type(n2) != int  and type(operator) != str:
#       print("Plese Enter Correct Numbers")
#    else:   

#       if operator == '+':
#          print(n1+n2)
#       elif operator == '-':
#          print(n1-n2)   
#       elif operator == '*':
#          print(n1*n2)   
#       elif operator == '/':
#          print(n1/n2)   
     
# calc(1,'*',8)  
# calc(1,'-',8)  
# calc(9,'/',3)  

# def say_hello(*peoples):  # n1, n2, n3, n4

#   for name in peoples:

#     print(f"Hello {name}")

# say_hello("Osama", "Ahmed", "Sayed", "Mahmoud")

# def show_details(name, *skills):

#   print(f"Hello {name} Your Skills Is: ")

#   for skill in skills:

#     print(skill)

# show_details("Osama", "Html", "CSS", "JS")
# show_details("Ahmed", "Html", "CSS", "JS", "Python", "PHP", "MySQL")

# def Add_Friends(*friend):
#    for f in friend:
#       print(f"-Your Frinds: {f}")
# Add_Friends("ahmed","ammar","kareem","faris")    
# 
# 
#   

# def calculate(Num1,Num2,Operator="+"):
#    Operator =  Operator.lower().strip()
#    if type(Num1) != int and  type(Num2) != int and type(Operator) != str:
#       print("Enter Correct Numbers") 
#    else:
#       if Operator == "a" or Operator == "add": 
#          return Num1 + Num2
#       elif Operator == "s" or Operator == "subtract":
#          return Num1 - Num2         
#       elif Operator == "m" or Operator == "multiply":
#          return Num1 * Num2            
# print(calculate(10,10,'a'))         
# print(calculate(30,10,'m'))   
# print(calculate(10,10,'s'))   
# print("-"*40)
# print(calculate(10,10,'AdD'))         
# print(calculate(10,10,'Multiply') )  
# print(calculate(30,10,'subTRACT'))  


# def addition(*Numbers):
#    Sum =  0
#    for num in Numbers:
#       if num == 10:
#          continue
#       elif num == 5:
#          Sum-= num
#       else:  
#          Sum+=num 

#    print(Sum) 

# addition(1,199,459) 


# def show_skills(Name,*Skills):
#    print(f"Hello {Name} Your Skills Is")
#    for skill in Skills:
#     print(f"-{skill}")
#    if skill == None :
#       print(f"Hello {Name} You Have No Skills To Show")
# show_skills("ahmed","SQL","Excel")
# show_skills("test","t","a")

# def say_hello(Name="Unknown",Age="Unknown",Country="Unknown"):
#    print(f"Hello {Name} Your Age Is {Age} And You Live In {Country}")
# say_hello("ahmed",20,"egypt")
# say_hello("ahmed",20)
# mySkills = {
#   'Html': "80%",
#   'Css': "70%",
#   'Js': "50%",
#   'Python': "80%",
#   "Go": "40%"
# }

# def show_skills(**skills):

#   for skill , value in skills.items():

#     print(f"{skill} => {value}")

# show_skills(**mySkills)

# skill = ("Excel","Sql","py","power bi")
# mySkills = {
#   'Go': "80%",
#   'Python': "50%",
#   'MySQL': "80%"
# }
# def detials(name,*skills,**mySkills):
#     print(f"Hi, {name}")
#     for skill in skills:
#         print(f"- {skill}")
#     for s in mySkills :
#         print(f"**{s}")    
# detials("ahmed",*skill,**mySkills) 


# mySkills = {
#   'Go': "80%",
#   'Python': "50%",
#   'MySQL': "80%"
# }

# def get_score(**mySkills):
#    for skill , value in mySkills.items():
#      print(f"{skill} => {value}")
# get_score(**mySkills)  
# print("-"*40)  
# get_score(Math=90, Science=80, Language=70) 

# mySkills = {
#   'Go': "80%",
#   'Python': "50%",
#   'MySQL': "80%"
# }
# def get_people_scores(*name,**skills):
#     print(f"Hello{name} This Is Your Score Table:") 
#     for skill , value in skills.items():
#        print(f"{skill} => {value}")


# get_people_scores("Osama", Math=90, Science=80, Language=70) 
# print("-"*40)
# get_people_scores("Mahmoud", Logic=70, Problems=60)
# print("-"*40)
# get_people_scores(Logic=70, Problems=60)
# print("-"*40)
# get_people_scores("Ahmed")
# print("-"*40)
# get_people_scores("ahmed",**mySkills)


# ------------------------
# -- Function Recursion --
# ------------------------
# ---------------------------------------------------------------------
# -- To Understand Recursion, You Need to First Understand Recursion --
# ---------------------------------------------------------------------

# Test Word [ WWWoooorrrldd ] # print(x[1:])

# def cleanWord(word):

#   if len(word) == 1:

#     return word

#   print(f"Print Start Function {word}")

#   if word[0] == word[1]:

#     print(f"Print Before Condition {word}")

#     return cleanWord(word[1:])

#   print(f"Print Before Return {word}")

#   return word[0] + cleanWord(word[1:])

#   # Stash [ World ]

# print(cleanWord("WWWoooorrrldd"))

# def get_score(**skills):
#     for skill , value in skills.items():
#         print(f"{skill} => {value}")
# get_score(Math=90, Science=80, Language=70)    
# get_score(Logic=70, Problems=60) 


# calc = lambda n1,n2: n1*n2
# print(calc(9,2))

# -------------------
# -- File Handling --
# -------------------
# "a" Append  Open File For Appending Values, Create File If Not Exists
# "r" Read    [Default Value] Open File For Read and Give Error If File is Not Exists
# "w" Write   Open File For Writing, Create File If Not Exists
# "x" Create  Create File, Give Error If File Exists
# --------------------------------------------------

import os

# Main Current Working Directory
# print(os.getcwd())

# Directory For The Opened File
# print(os.path.dirname(os.path.abspath(__file__)))

# # Change Current Working Directory
# os.chdir(os.path.dirname(os.path.abspath(__file__)))

# print(os.getcwd())

# print(os.path.abspath(__file__))

# file = open(r"D:\Python\Files\nfiles\osama.txt")

file = open(r"D:\Python\Project\ahmed.txt","r")

# Data Object
# print(file.name)
# print(file.mode)
# print(file.encoding)

# print(file.read())

# print(file.read(20))
# print(file.readline(1))
# print(file.readline(2))



# -----------------------------------------------
# -- File Handling => Write and Append In File --
# -----------------------------------------------

# myFile = open(r"D:\Python\Project\taha.txt", "w")
# myFile.write("Hello\n")
# myFile.write("Third Line")

# myFile = open(r"D:\Python\Project\taha.txt", "w")
# myFile.write("Elzero Web School\n" * 1000)

# myList = ["Oasma\n", "Ahmed\n", "Sayed\n"]

# myFile = open(r"D:\Python\Project\taha.txt", "w")
# myFile.writelines(myList)

# myFile = open(r"D:\Python\Project\taha.txt", "a")
# myFile.write("Elzero")