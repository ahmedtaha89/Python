# mylist =  [1,2,3,54,0,()]
def  my_all(*l):
    for a in l :
     if bool(a[0:-1]) == True:
         return "True"
     else:
          return False   
    

print(my_all(1,2,3,54,0,()))


 
 # ------------------------
# -- Built In Functions --
# ------------------------
# abs() => | |  => القيمه المطلقه => return positive number
# pow() => power
# min()
# max()
# slice()
# ------------------------


a = -100
b = -0.54
c = 5
print(abs(a))
print(abs(b))
print(abs(c))

# pow(base, exp, mod || %)
print(pow(2,2,2))


# min(item, item , item, or iterator) => اقل قيمه 
test_min = [84,89,448,4,77,-1,44] 
print(min(test_min))

# max(item, item , item, or iterator) => اكبر قيمه 
myNumbers = (1, 20, -50, -100, 100)
print(max(myNumbers))

# not include end
# slice(start, end, step) => لازم تحدد النهايه

a = ["A", "B", "C", "D", "E", "F"]
print(a[:-1])
print(a[2:-1])
print(a[0:])


print(a[slice(2,-1)])
 
 