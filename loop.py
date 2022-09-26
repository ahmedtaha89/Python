# def show_skills(name,*skills):
#     print(f"Hello {name} Your Skills Is")
#     for s in skills:
#       print(f"-{s}")
# show_skills("ahmed","Python","SQL")
# show_skills("Osama", "HTML", "CSS", "JS", "Python")


# ----------------------------------------------------
# -- Function Packing, Unpacking Arguments **KWArgs --
# ----------------------------------------------------

# **KWArgs => dictionary 

# mySkills = {
#     'Html': "80%",
#     'Css': "70%",
#     'Js': "50%",
#     'Python': "80%",
#     "Go": "40%"
# }


# def show_skills(**skills):
#     print(type(skills))
#     for s_key,s_value in skills.items():
#         print(f"-{s_key} => {s_value}")


# show_skills(mySkills)

# mySkills = {
#     'Go': "80%",
#     'Python': "50%",
#     'MySQL': "80%"
# }

# T = ("python", "oop", "sql","Design database")

# def show_skills(name, *skills, **skillsWithProgres):
#     a = 0
#     print(f"Hi, {name} , \n Skills Without Progress Is:")
#     for s  in skills:
#         a+=1
#         print(f"{a}) {s}")
        
#     print("\n")
    
#     print("Skills Progress Is:")
#     for s_key, s_value in skillsWithProgres.items():
#         print(f"{s_key} => {s_value}")
        
# show_skills("Ahmed" ,*T,**mySkills)    




# --------------------
# -- Function Scope --
# --------------------

# global => اقدر استدعيها في اي مكان
# global + varible => global بجبر المغير ده انه يكون 

x = 5 

def test_one():
    
    # x => local
    x=15
    print(f"Print Variable From Function Scope {x}")
    
def test_two():
    
    # x => local
    global x
    x=1
    
    print(f"Print Variable From Function Scope {x}")
    

test_two()
print(f"global: {x}")
test_one()
print(f"Print Variable From Global Scope After One Function Is Called {x}")

# 5 15 1 5
# 5 15 1 1
# 1 1 15 1