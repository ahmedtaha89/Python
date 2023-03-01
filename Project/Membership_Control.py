# Admin = ["ahmed","ammar","faris","eslam"]
# Name  = str(input("Enter Your Name: ")).strip().lower()
# if Name in Admin:
#     print(f"Welcome, {Name}")

#     option = str(input("Delete Or Update Your Name ?")).strip().lower()

#     if option == "update" or option =="u":
#         NewName = str(input("Enter Your New Name: "))
#         Admin[Admin.index(Name)] = NewName
#         print(f"Your Name Updated {NewName}")
#         print(Admin)

#     elif option == "delete" or option =="d":
#         # NewName = str(input("Enter Your New Name: "))
#         Admin.remove(Name) 
#         print(f"Your Name Updated {Name}")
#         print(Admin)



# else :
#     print("You Aren't Admin.")    

# count  = 0
# num = int(input("Enter The Number: "))
# if num == 0 :
#     print("Number 0 Is Not Larger Than 0")
# else: 
#     while num > 0  :
        
#         num-=1 

#         if num == 6:
#             continue

#         elif num == 0:
#             break  

#         print(num) 

#         count+=1

#     print(f"{count} Numbers Printed Successfully.")   


# friends = ["Ahmed", "Kareem", "ahmed" , "Ammar", "faris"]
# count = 0
# a = 0
# while a < len(friends):
#    if friends[a].istitle():
#     print(friends[a])
# a +=1

# # Code
# skills = ["HTML", "CSS", "JavaScript", "PHP", "Python"]

# while skills:
#     print(skills if len(skills)<5 else "")
  # Input
# Input
# Input
# Input
students = {
  "Ahmed": {
    "Math": "A",
    "Science": "D",
    "Draw": "B",
    "Sports": "C",
    "Thinking": "A"
  },
  "Sayed": {
    "Math": "B",
    "Science": "B",
    "Draw": "B",
    "Sports": "D",
    "Thinking": "A"
  },
  "Mahmoud": {
    "Math": "D",
    "Science": "A",
    "Draw": "A",
    "Sports": "B",
    "Thinking": "B"
  }
}

grade = 0
Sum = 0 
for student in students:
    print("------------------------------")
    print(f"-- Student Name => {student}")
    print("------------------------------")
    
    for key in students[student] :
        
        if students[student][key] == 'A':
                grade = 100
        
        elif students[student][key] == 'B':
                grade = 80
          
        elif students[student][key] == 'C':
               grade = 40
          
        elif students[student][key] == 'D':
               grade = 20

               
        Sum+= grade               
        print(f"{key} => {grade} Points")
        
    print(f"Total Points For {student} Is {Sum}")
        

