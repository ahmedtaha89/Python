Age = int(input("Enter Your Age: "))
unit = str(input("Please Choose Time Unit: All , Months, Weeks, Days or (m , w , d): ")).strip().lower()

Months = Age * 12
Weeks = Months * 4
Days = Weeks * 365

if unit == "months" or unit == "m":
    print(f"You Lived For {Months} Months")

elif  unit == "weeks" or unit == "w":
    print(f"You Lived For {Weeks} Weeks")  

elif  unit == "days" or unit == "d":
    print(f"You Lived For {Days:,} Days")   

elif  unit == "all" or unit == "a":
    print(f"You Lived For {Age} Age {Months} Months , {Weeks} Weeks , {Days:,} Days")       