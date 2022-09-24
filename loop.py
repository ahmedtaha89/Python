# F_loop = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for loop in F_loop:
#     if loop % 2 == 0:
#         print(f"Even:{loop}")
#     elif loop % 2 != 0:
#         print(f"Odd:{loop}")
# else :
#     print("Done")

# t = 'ahmed taha'
# a = 0
# for test in t:
#     a+=1
#     print(f"({a}){test}*2".strip().capitalize())

# r = range(1,11)
# for R in  r  :
#     print(R)



# peoples = ["Osama", "Ahmed", "Sayed", "Ali"]
# skills = ['Html', 'Css', 'Js']

# for p in peoples :
#     print(f"{p} skills:")
# for s in skills :
#     print(s)

# Dictionary

# peoples = {
#     "Osama": {
#         "Html": "70%",
#         "Css": "80%",
#         "Js": "70%"
#     },
#     "Ahmed": {
#         "Html": "90%",
#         "Css": "80%",
#         "Js": "90%"
#     },
#     "Sayed": {
#         "Html": "70%",
#         "Css": "60%",
#         "Js": "90%"
#     }
# }

# print(peoples["Osama"])
# print(peoples["Ahmed"])
# print(peoples["Sayed"])

# print(peoples["Osama"]['Css'])
# print(peoples["Ahmed"]['Css'])
# print(peoples["Sayed"]['Css'])

# for name in peoples:

#   print(f"Skills and Progress For {name} Is: ")

#   for skill in peoples[name]:

#     print(f"{skill.upper()} => {peoples[name][skill]}")

# x = 7
# x ^= 3 # x = x^3 =5^3
# print(x)


# F_loop = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for loop in F_loop:
#     if loop % 2 == 0:
#         pass
# print(f"Even:{loop}")




# mySkills = {
#     "HTML": "80%",
#     "CSS": "90%",
#     "JS": "70%",
#     "PHP": "80%"
# }

# for skill in mySkills:

#   print(f"{skill} => {mySkills[skill]}")


# for s_key ,s_value in mySkills.items():
#  print(f"Key:{s_key} , value{s_value}")
  
#  for skill_key, skill_progress in mySkills.items():

#   print(f"{skill_key} => {skill_progress}")


# my_nums = [15, 81, 5, 17, 20, 21, 13]
# my_nums.sort(reverse=True)
# a = 0
# for n in my_nums:
#     if n % 5 == 0:
#         a += 1
#         print(f"{a}=>{n}")
# print("All Numbers Printed")
# r = range(1,21)

# for x in range(1,21) :
#     if x in [6,8,11]:
#         continue
#     elif x < 10:
#         print(f"\"0{x}\"")
#     else:
#      print(f"\"{x}\"")

# print("All Numbers Printed")   

# students = {
#     "Ahmed": {
#         "Math": "A",
#         "Science": "D",
#         "Draw": "B",
#         "Sports": "C",
#         "Thinking": "A"
#     },
#     "Sayed": {
#         "Math": "B",
#         "Science": "B",
#         "Draw": "B",
#         "Sports": "D",
#         "Thinking": "A"
#     },
#     "Mahmoud": {
#         "Math": "D",
#         "Science": "A",
#         "Draw": "A",
#         "Sports": "B",
#         "Thinking": "B"
#     }
# }

# for s_key,s_value in students.items() :

#     print(f"Student Name= > {s_key}")
#     total = 0
#     for v in s_value:
#         if s_value[v] == "A":
#            s_value[v] = 100
           
#         elif s_value[v] == "B":
#            s_value[v] = 80
           
#         elif s_value[v] == "C":
#            s_value[v] = 40
           
#         elif s_value[v] == "D":
#            s_value[v] = 20
    
#         print(f"{v} => {s_value[v]} Points")
       
#         total+=s_value[v]
#     print(f"Total Points For {s_key} Is {total}")
#     print("-"*30)


# my_ranks = {
#     'Math': 'A',
#     "Science": 'B',
#     'Drawing': 'A',
#     'Sports': 'C'
# }

# rank = {
#     'Math': 100,
#     "Science": 80,
#     'Drawing': 100,
#     'Sports': 60
# }

 # if my_ranks[r_value] == "A":
    #    my_ranks[r_value] = 100

    # elif my_ranks[r_value] == "B":
    #  my_ranks[r_value] = 80

    # elif my_ranks[r_value] == "C":
    #  my_ranks[r_value] = 40

    # elif my_ranks[r_value] == "D":
    #  my_ranks[r_value] = 20
# for r_key, r_value in my_ranks :
#     total = 0
#     print(
#         f"My Rank in {r_key} Is {r_value} And This Equal {my_ranks[r_value]} Points")
    # total += my_ranks[rank]
# print(f"Total Points Is {total}")


my_ranks = {
    'Math': 'A',
    "Science": 'B',
    'Drawing': 'A',
    'Sports': 'C'
}

rank = {
    'A':100,
    "B":80,
    'C': 70
}
total = 0
for r_key, r_value in my_ranks.items() :
    print(
        f"My Rank in {r_key} Is {r_value} And This Equal {rank[r_value]} Points")
    total += rank[r_value]
print(f"Total Points Is {total}")
