# ------------------------
# -- Built In Functions --
# ------------------------
# sum()
# round()
# range()
# print()
# ------------------------


# sum(iterable, start)
# iterable => list || tuple || set 
# start الرقم اللي هجمعه عليهم  
from email.policy import default


l = [1,2,3,4,5]
print(sum(l))
print(sum(l,15))


# round(number, numofdigits) =>    بستخدمها عشان اقرب الارقام
print(round(99.661,2))


# range(start, end, step) => بحدد البدايه و النهايه و عدد الخطوات
# step(default) = 1

# for a in range(1,11):
#     a=0
#     # a+=1
#     print(a)



# for a in range(1,11,2):
#     a=0
#     # a+=1
#     print(a)



# print()

# end(default) = "\n"
# print("First" , end="\t" )
# print("Second")
# print("third")

print("Hello @ Osama @ How @ Are @ You")
# sep = "space" == " "


print("Hello", "Osama", "How", "Are", "You", sep=" - ")      