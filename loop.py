# def get_score(**Subjects):
#     for s_key , s_value in Subjects.items():
#       print(f"{s_key}=>{s_value}")
    

# get_score(Math=90, Science=80, Language=70)
# get_score(Logic=70, Problems=60)

# def get_people_scores(name="ahmed",**Subjects):
#         if  len(Subjects)>0:
#          print(f"Hello {name} This Is Your Score Table:")
#         else:
#           print(f"Hello {name} You Have No Scores To Show")   
#         for s_key , s_value in Subjects.items():
#             print(f"{s_key}=>{s_value}")
         
        

# # Test1
# get_people_scores("taha",Math=90, Science=80, Language=70)  
   
# # Test2
# get_people_scores("Mahmoud", Logic=70, Problems=60)

# # Test3 
# get_people_scores(Logic=70, Problems=60)

# # Test4
# get_people_scores("Ahmed")








skills = {
"Math" : 90,
"Science" : 80,
"Language" : 70

}

def get_people_scores(name="",**skills):
    if bool(name) == True:
     print(f"Hello {name} This Is Your Score Table:")
     
     for s_key , s_value in skills.items() : 
         print(f"{s_key}=>{s_value}")
    else :     
       for s_key , s_value in skills.items() : 
         print(f"{s_key}=>{s_value}")
         
get_people_scores("ahmed",**skills)
print("\n")         
get_people_scores(**skills)         
