# OOP    => Object Oriented Programming
# OOP    => Paradigm or Coding Style
# OOP    =>  Help to make code readable and reuseable 
# Class  => Template or Blueprint for create object
# Object => Copied of class have attributes and methods

# To create class (syntax)

# (class) keyword
# class <Name class>
#     Constructor => Do Instantiation [ Create Instance From A Class ]
#     Each Instance Is Separate Object
#     def __init__(self, other_data)
#         Body Of Func

# self => refer to current instance



class Member:
  def __init__(self, first_name, middle_name, last_name):
    self.fname = first_name
    self.mname = middle_name
    self.lname = last_name

member_one = Member("Osama", "Mohamed", "Elsayed")
member_two = Member("Ahmed", "Ali", "Mahmoud")
member_three = Member("Mona", "Ali", "Mahmoud")

# print(dir(member_one))

print(member_one.fname, member_one.mname, member_one.lname)
print(member_two.fname)
print(member_three.fname)