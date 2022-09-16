# favorite subject

favorite_subject = 5
subject  = []

while favorite_subject > 0 : 
  s = input("Enter  your favorite subject: ").strip().lower()
  subject.append(s)
  favorite_subject -= 1
  print("favorite subject added.")
  print(subject)
  print(f" you can add {favorite_subject} subject.")
  
else : 
    print("Sorry you can`t added new subject")
