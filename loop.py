
# from modulefinder import Module
# import random 
# print(random)
# print(f"Print Random Float Number {random.random()}")


# Show All Functions Inside Module
# print(dir(random))


# # Import One Or Two Functions From Module
# from random import randint, random
# print(f"Print Random Float {random()}")
# print(f"Print Random Integer {randint(100, 900)}")




import Test_module as md

# print(dir(md))
md.sayHi("ahmed")
md.enterGpa(3.2)




from  Test_module import sayHi 
md.sayHi("ali")