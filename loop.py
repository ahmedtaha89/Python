# mylist =  [1,2,3,54,0,()]
def  my_all(*l):
    for a in l :
     if bool(a[0:-1]) == True:
         return "True"
     else:
          return False   
    

print(my_all(1,2,3,54,0,()))


