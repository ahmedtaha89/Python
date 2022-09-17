#  -------------------------------
#  Information About File
#  License
#  Who Created The File
#  When The File Created
#  Why The File Created
#  Write Beside The Programming Line
#  Write Before The Programming Line
#  Prevent Code From Run
#  -------------------------------


print("I Love Python")  # This is Inline Comment
print("Programming")  # I Used This Method Because of Bla Bla Bla
print("Programming")  # If You Used Test Method Will Through Error


# this is not comment
"""
This is
Not
Multiple
Line
Comments
"""

#  ----------------------------
#  type()
#  All Data in Python is Object
#  ----------------------------

print(type(10))  # int => Integer
print(type(100))  # int => Integer
print(type(-50))  # int => Integer

print(type(100.9))  # float => Floating Point Number
print(type(1.0950950))  # float => Floating Point Number
print(type(-100.9595))  # float => Floating Point Number

print(type("Hello Python"))  # str => String

print(type([1, 2, 3, 4, 5]))  # list => List

print(type((1, 2, 3, 4, 5)))  # tuple => Tuple

print(type({"One": 1, "Two": 2, "Three": 3}))  # dict => Dictionary

print(type(2 == 20))  # bool => Boolean


#  --------------------------------------
#  -- Variables --
#  ---------------
#  Syntax => [Variable Name] [Assignment Operator] [Value]
#
#  Name Convention and Rules
#  [1] Can Start With (a-z A-Z) Or Underscore
#  [2] You Cannot With Num Or Special Characters
#  [3] Can Include (0-9) Or Underscore
#  [4] Cannot Include Special Characters
#  [5] Name is Not Like name [ Case Sensitive ]
#  --------------------------------------

name = "Osama Elzero"  # Single Word => Normal
myName = "Osama Elzero"  # Two Words => camelCase
my_name = "Osama Elzero"  # Two Words => snake_case

print(name)
print(myName)
print(my_name)

# variable
x = 5
y = "test"
z = 4

print(x)
print(y)
print(z)
print(x+z)

x = 4  # x is of type int
x = "Sally"  # x is now of type str
print(x)


# Camel Case
# Each word, except the first, starts with a capital letter:
# myVariableName = "John"

# Pascal Case
# Each word starts with a capital letter:
# MyVariableName = "John"

#  Snake Case
# Each word is separated by an underscore character:
# my_variable_name = "John"


# Many Values to Multiple Variables
# Python allows you to assign values to multiple variables in one line:
# Example
# x, y, z = "Orange", "Banana", "Cherry"

#  print(x)
#  print(y)
#  print(z)


x = "Python "
y = "is "
z = "awesome"
print(x, y, z)


#  Declare a variable and initialize it
f = 101
print(f)


#  ---------------
#  -- Variables --
#  ---------------
#  Source Code : Original Code You Write it in Computer
#  Translation : Converting Source Code Into Machine Language
#  Compilation : Translate Code Before Run Time
#  Run-Time : Period App Take To Executing Commands
#  Interpreted : Code Translated On The Fly During Execution
#  --------------------------------------------------------

#  Reserved Words
help("keywords")

a, b, c = 1, 2, 3

print(a)
print(b)
print(c)

print("Hello\ttest")

print("123\r321")
print("\x41\x48\x4D\x45\x44 \x54\x41\x48\x41")

savings = 100
result = 100 * 1.10 ** 7
print("I started with $" + str(savings) +
      " and now have $" + str(result) + ". Awesome!")

#  -------------------
#  -- Concatenation --
#  -------------------

First_Name = "Ahmed "
Last_Name = "Taha"
Name = First_Name + "\n" + Last_Name
print(Name)
print(First_Name + " " + Last_Name)
#  print("Hello " + 1)  #  Error

#  -------------
#  -- Strings --
#  -------------
First_string = "Test_1"
Second_string = 'Test_2'
print(First_string)
print(Second_string)


First_string = "Test 'one' "
Second_string = 'Test "two" '

print(First_string)
print(Second_string)

print('''First
Second 'Test' "Test"
Third''')

print("""First
Second "Test" \\\ 'Test'
Third""")


#  ---------------------------------
#  Strings Indexing & Slicing
#  [1] All Data in Python is Object
#  [2] Object Contain Elements
#  [3] Every Element Has Its Own Index
#  [4] Python Use Zero Based Indexing ( Index Start From Zero )
#  [5] Use Square Brackets To Access Element
#  [6] Enable Accessing Parts Of Strings, Tuples or Lists
#  ---------------------------------

#  Indexing ( Access Single Item )

myString = "Access Single Item"
print(myString[::4])


# Slicing ( Access Multiple Sequence Items )
# [Start:End] End Not Included
# [Start:End:Steps]

print(myString[8:11])  # yth
print(myString[3:5])  # ov

print(myString[:10])  # If Start Is Not Here Will Start From 0 (I Love Pyt)
print(myString[5:])  # If End Is Not Here Will Go To The End (e Python)
print(myString[:])  # Full Data

#  ---------------------
#  -- Strings Methods --
#  ---------------------

#  strip() rstrip() lstrip()

a = "    I Love Python    "
print(a.strip())
print(a.rstrip())
print(a.lstrip())

a = "# # # # # I Love Python# # # # "
print(a.strip("# "))
print(a.rstrip("# "))
print(a.lstrip("# "))

a = "@# @# @# I Love Python@# @# @# "
print(a.strip("@# "))
print(a.rstrip("@# "))
print(a.lstrip("@# "))

#  title()

b = "I Love 2d Graphics and 3g Technology and python"
print(b.title())

#  capitalize()

b = "I Love 2d Graphics and 3g Technology and python"
print(b.capitalize())

#  zfill

c, d, e, f = "1", "11", "111", "1111"

print(c)
print(d)
print(e)
print(f)

print(c.zfill(4))
print(d.zfill(4))
print(e.zfill(4))
print(f.zfill(4))

#  upper()

g = "osama"

print(g.upper())

#  lower()

h = "OSama"

print(h.lower())

#  ---------------------
#  -- Strings Methods --
#  ---------------------

#  split() =>  separator and step و بتستقبل حاجه اسمها list بتفصل الكلام و ترجعه في
#  rsplit()

#  default
a = "I Love Python and PHP and MySQL"
print(a.split())

#  separator
a = "I_Love_Python_and_PHP_and_MySQL"
print(a.split("_"))

#  separator and step
a = "I_Love_Python_and_PHP_and_MySQL"
print(a.split("_", 3))

#  separator and step
a = "I_Love_Python_and_PHP_and_MySQL"
print(a.rsplit("_", 3))


#  center() بتضيف قبل و بعد الكلام اي حاجه انت عايزها
#  لازم تحدد عدد الحروف اللي هضيفها و عدد حروف الكلمه نفسها
#  وبعدين الحرف اللي عايز تضيفه

v = "Ahmed"
print(v.center(11, "*"))
print(v.center(15, "@"))  # @


#  count() بتعد الكلمه موجوده كام مره في النص
#  لازم تحدد الكلمه اللي هيدور عليها
#  count(word, start, end))

f = "I Love Python and PHP Because PHP is Easy"
print(f.count("PHP"))
print(f.count("PHP", 0, 10))

#  swapcase() small => capital بتبدل الحرف
g = "I Love Python"
h = "i lOVE pYTHON"

print(g.swapcase())
print(h.swapcase())


#  startswith("char, start , end") بتحقق من اول حرف لو طلع هو بيرجع ترو مكنش فولس
i = "I Love Python"
print(i.startswith("I"))
print(i.startswith("S"))
print(i.startswith("P", 7, 12))

#  endswith("char, start , end") بتحقق من اخر حرف لو طلع هو بيرجع ترو مكنش فولس
print("\n")
print(i.endswith("n"))
print(i.endswith("S"))
print(i.endswith("n", 7, -1))


#  ---------------------
#  -- Strings Methods --
#  ---------------------

#  index(SubString, Start, End) return the index

a = "I Love Python"
print(a.index("n"))
print(a.index("o", 0, 15))

#  find() =>  index() بس الاختلاف لو الحرف اللي بتبحث عنه مش موجود بيرجع -1
b = "I Love Python"
print(b.find("lo"))

#  rjust("width, fill char")   ||   ljust("width, fill char")   ||   center("width, fill char")  =>  بيضيفوا قبل الكلمه

c = "Ahmed"
print(c.center(15, "!"))

#  rjust() add fill char from right
print(c.rjust(10, "!"))

#  ljust() add fill char from left
print(c.ljust(10, "!"))

#  splitlines() list  بقدر اقسم السطور اللي عندي و اخزمهم في

e = """First Line
Second Line
Third Line"""

print(e.splitlines())

d = "Ahmed \n Taha \n Ahmed"
print(d.splitlines())

# expandtabs("number spaces")  add tab betweens the words
f = " I\t  Love\t Python\t  And \t 3G "
print(f.expandtabs(5))

# islower() check the text is lower
g = "my name Ahmed"
print(g.islower())

# islower() check the text is upper
g = "MY NAME AHMED TAHA"
print(g.isupper())

# istitle() check the text is title
h = "Ahmed Taha 89Fci"
print(h.istitle())

# isspace() is checking there the space
print("\n")
s = " "
print(s.isspace())

print("\n")
s = ""
print(s.isspace())

# isidentifier()  check the text can used to a variable

v = "_ahmed_taha"
b = "Ahmed89taha"
n = "#ahmed-taha"
m = "89ahmedtaha"

print("\n")
print(v.isidentifier())
print(b.isidentifier())
print(n.isidentifier())
print(m.isidentifier())

print("\n")
x = "AaaaaBbbbbb"
y = "AaaaaBbbbbb111"
print(x.isalpha())
print(y.isalpha())


print("\n")
u = "AaaaaBbbbbb"
z = "AaaaaBbbbbb111"
print(u.isalnum())
print(z.isalnum())

# replace("old word" , "new word" , count ) replace the old word to new word
name = "ahmed taha ahmed"
print(name.replace("ahmed", "taha"))
print(name.replace("ahmed", "taha", 1))


# join(Iterable) => split  دي عكس
name = ["ahmed", "taha", "ahmed"]
print("_".join(name))

# ------------------------------------
# -- Strings Formatting (Old Way)-----
# ------------------------------------

name = "Ahmed"
age = 20
gpa = 3

print("My Name is: " + name)
# print("My Name is: " + name + " " + age) # type error


# %s  => String
# %d  => Number
# %f  => Float

print("My Name is: %s" % "ahmed")
print("My Name is: %s" % name)
print("My Name is: %d" % age)
print("My Name is: %f" % gpa)
print("my name is  %s and my age %d and my gpa  is : (%f) " % (name, age, gpa))


Name = "Ahmed Taha"
Age = 20
Job = "Data Analyst"
Salary = 5000
print("My Name is %s and Iam %d years and my job %s" % (Name, Age, Job))

# Control Floating Point Number
print("my name is  %s and my age %d and my gpa  is : (%.2f) " % (name, age, gpa))
print("My Name is %s and Iam %d years and my salary  %.3f" % (Name, Age, Salary))


# Truncate String
Name = "Ahmed Taha"
print("My name is %.5s" % Name)


# ------------------------------------
# -- Strings Formatting (New Way)-----
# ------------------------------------

# {:s}  => String
# {:d}   => Number
# {:f}   => Float
print("\n")
print("My Name is: {:s}"  .format("ahmed"))
print("\n")
print("My Name is: {:s}"  .format(name))
print("\n")
print("My Name is: {:d}"  .format(age))
print("\n")
print("My Name is: {:f}"  .format(gpa))
print("\n")
print("my name is   {:s} and my age {:d} and my gpa  is : ({:f}) " .format(
    name, age, gpa))
print("\n")

Name = "Ahmed Taha"
Age = 20
Job = "Data Analyst"
Salary = 5000
print("\n")
print("My Name is {:s} and Iam {:d} years and my job {:s}" .format(
    Name, Age, Job))
print(f"My Name is {Name} and Iam {Age} years and my job {Job}")
print("\n")

# Control Floating Point Number
print("\n")
print("my name is  {:s} and my age {:d} and my gpa  is : {:f} " .format(
    name, age, gpa))
print("\n")
print("My Name is {:s} and Iam {:d} years and my salary  {:.2f}" .format(
    Name, Age, Salary))


# Truncate String
Name = "Ahmed Taha"
print("\n")
print("My name is {:.5s} " .format(Name))
print("\n")


# Money Format
myMoney = 500162350198
print("My Money in Bank Is: {:d}"  .format(myMoney))
print("My Money in Bank Is: {:,d}"  .format(myMoney))
print("My Money in Bank Is: {:_d}"  .format(myMoney))

# ReArrange Items
a = 1
b = 2
c = 3
print("one: {2} , \t Two : {0} , \t Three {1}" .format(a, b, c))


a = 1000
b = 2000
c = 3000
print("one: {2:f} , \t Two : {0:f} , \t Three {1:f}" .format(a, b, c))
print("one: {0:.3f}  \t Two : {1:.3f}  \t Three {2:.3f}" .format(a, b, c))

# List

test = "test " * 8
print(test)


print([1, 2, 3] * 3)


# -------------
# -- Numbers --
# -------------

# Integer =>  رقم صحيح سواء موجب أو سالب

print(type(1))
print(type(-1))
print(type(1111))

print("\n")

# Float (Floating point number)  =>  رقم غير صحيح يعني يحتوي علي كسور سواء موجب او سالب

print(type(1.006))
print(type(-1.549))
print(type(1454.123456789))
print(type(-1454.123456789))
print("\n")

# Complex  (Real Number + imaginary Number)

print(10+5j)
print(type(10+5j))

Complex = 5+9j
print(f"Real Num is :{Complex.real}")
print(f"imaginary Num is :{Complex.imag}")
print("\n")


# [1] You Can Convert From Int To Float or Complex

print(100)
print(float(100))
print("\n")


# [2] You Can Convert From Float To Int or Complex

print(10.0)
print(int(10.0))

# [3] You Can Convert From Float To Int or Complex

print(10.05)
print(complex(10.05))

# [4] You Cannot Convert Complex To Any Type


print(5+5j)
# print(int(5+5j))


# --------------------------
# -- Arithmetic Operators --
# --------------------------
# [+] Addition
# [-] Subtraction
# [*] Multiplication
# [/] Division
# [%] Modulus
# [**] Exponent
# [//] Floor Division
# --------------------------

# [+] Addition

print(9 + 9)
print(9.5 + 9)
print(-91 + 900)


# [-] Subtraction

print(9 - 9)
print(9.5 - 9)
print(91 - 900)

# [*] Multiplication

print(9 * 9)
print(9.5 * 9)
print(-12 * 9)

# [/] Division

print(-9 / 9)
print(9.5 / 9.5)
print(12 / 2)

# [%] Modulus

print(3 % 2)
print(4 % 2)
print(9 % 2)

# [**] Exponent

print(3 ** 2)
print(-4 ** 2)
print(9.5 ** 2)

# [//] Floor Division  => بتاخد  الرقم الصحيح بعد  القسمه

print(100 // 20)  # 5
print(119 // 20)  # 5
print(120 // 20)  # 6
print(140 // 20)  # 7
print(142 // 20)  # 7print(100 // 20)  # 5
print(119 // 20)  # 5
print(120 // 20)  # 6
print(140 // 20)  # 7
print(142 // 20)  # 7
print([1, 2, 3] * 3)


# -----------------------------
# -- Lists --
# -----------
# [1] List Items Are Enclosed in Square Brackets
# [2] List Are Ordered, To Use Index To Access Item
# [3] List Are Mutable => Add, Delete, Edit
# [4] List Items Is Not Unique
# [5] List Can Have Different Data Types
# -----------------------------


List = ["ahmed", 89, "taha", True, True, 89.63]
print(List)
print(type(List))
print(List[0])
print(List[-1])
# slicing
print(List[-3:-1])
print(List[0:3])
print(List[0:])
print(List[:-1])
# indexing
print(List[::3])
print(List[::-2])
List[3] = "Ahmed"
print(List[3])
List[0] = "Ahmed"
print(List[0:4])
List[1:4] = ["Test"]
print(List)

# -------------------
# -- Lists Methods --
# -------------------

# append()  list بتضيف عنصر في نهايه

name = ["Ahmed", "Taha", "Ahmed"]
name.append("El bastawesy")
print(name)
name.append(89.6)
print(name)
name.append(True)
print(name)

name = ["Ahmed", "Taha", "Ahmed"]
bro = ["mostafa", "Taha", "Ahmed"]
name.append(bro)
print(name)
print(name[3][0])


# extend()  =>  list بتعمل دمج ل
name = ["Ahmed", "Taha", "Ahmed"]
bro = ["mostafa", "Taha", "Ahmed"]
bro_2 = ["mohmed", "taha", "ahmed"]
name.extend(bro)
name.extend(bro_2)
print(name)

# remove() remove item from list
bro = ["mostafa", "Taha", "Ahmed"]
bro.remove("Ahmed")
print(bro)

# sort()   من حيث الاكبر او الاصغر  list بتعمل فرز

y = [1, 2, 100, 120, -10, 17, 29]
y.sort()
print(y)

# sort(reverse = True || False)

y.sort(reverse=True)  # Sort اللي اتعملها  list بتعكس
print(y)


# reverse() =>  list بتعكس

y = [1, 2, 100, 120, -10, 17, 29]
y.reverse()
print(y)


# -------------------
# -- Lists Methods --
# -------------------

# clear()  =>  list من items بتفضي كل

a = [1, 2, 8, "fd", True]
a.clear()
print(a)

# List_Name[]  = []  => Clear

# copy()  =>  تانيه list ل list اللي في items بتنسخ كل

b = [1, 2, 3, 4, 5, 6, 7]
c = b.copy()
b.append(8)
print(b)  # Main List
print(c)  # Copied List


# count() => كام مره items بتعد
d = [1, 2, 3, 4, 3, 9, 10, 1, 2, 1]
print(d.count(1))


# index()  => Return index  item

e = ["Osama", "Ahmed", "Sayed", "Ramy", "Ahmed", "Ramy"]
print(e.index("Ahmed"))

# insert("index","value") add before Item  that you selected
f = [1, 2, 3, 4, 5, "A", "B"]
f.insert(0, 0)
print(f)

# pop(index) remove item from list and return the list
g = [1, 2, 3, 4, 5, "A", "B"]
g.pop(0)
print(g)


# -----------------------------
# -- Tuple --
# -----------
# [1] Tuple Items Are Enclosed in Parentheses
#  [2] You Can Remove The Parentheses If You Want
# [3] Tuple Are Ordered, To Use Index To Access Item
# [4] Tuple Are Immutable => You Cant Add or Delete
# [5] Tuple Items Is Not Unique
# [6] Tuple Can Have Different Data Types
# [7] Operators Used in Strings and Lists Available In Tuples
# -----------------------------

# Tuple syntax

Tuple = ("Ahmed", "Taha")
# Tuple = "Ahmed"
# Tuple[0] = "Taha"  not support item assignment
# Tuple[1] = []      not support item assignment
Tuple = (1.55, 10, 1121, "Test", True, 1.55, [1, 2, 3, 4, 5])
print(Tuple)
print(type(Tuple))


# Tuple Indexing

print(Tuple[3])
print(Tuple[6][2])
print(Tuple[-2:])
print(Tuple[0::2])

# -----------
# -- Tuple --
# -----------


# Tuple With One Element

Test_one = ("Ahmed Taha",)
Test_two = "Ahmed Taha",

print(type(Test_one))
print(type(Test_two))


# len  =>  او الحروف لو كلمه واحده Tuple بترجع عدد العناصر في
_Length_1 = (1.55, 10, 1121, "Test", True, 1.55, [1, 2, 3, 4, 5])
print(len(_Length_1))
_Length_2 = "Ahmed Taha"
print(len(_Length_2))


# Tuple Concatenation
a = (1, 2, 3, 4)
b = (5, 6)
c = a + b
print(c)

c = a + ("Ahmed", 55, True) + b
print(c)

# Tuple Repeat (*)
Test_List_Repeat = ("Ahmed ",) * 3
print(Test_List_Repeat)

# List Repeat (*)
Test_tuple_Repeat = [1, 2]
print(Test_tuple_Repeat)

# String Repeat (*)
Test_string_Repeat = "Ahmed " * 3
print(Test_string_Repeat)


# Methods => count() => count items is tuple
Test_count = (1.55, 10, 1121, "Test", True, True, True, 1.55, [1, 2, 3, 4, 5])
print(Test_count.count(True))

# Methods => index() => return index from tuple
Test_index = (1.55, 10, 1121, "Test", True, True, True, 1.55, [1, 2, 3, 4, 5])
print(Test_index.index(10))


b = (1, 3, 7, 8, 2, 6, 5)
# print("The Position of Index Is: " + b.index(7))  # Error
# Old way string format
print("The Position of Index Is: %d" % (b.index(7)))

# New way string format
print("The Position of Index Is: {:d}" .format(b.index(7)))
# New way string format => Js
print(f"The Position of Index Is: {b.index(7)}")


# Tuple Destruct
a = ("A", "B", 4, "C")
x, y, _, z = a
print(x)
print(y)
print(z)


# -----------------------------
# -- Set --
# ---------
# [1] Set Items Are Enclosed in Curly Braces
# [3] Set Indexing and Slicing Cant Be Done
# [4] Set Has Only Immutable Data Types (Numbers, Strings, Tuples) List and Dict Are Not
# [2] Set Items Are Not Ordered And Not Indexed
# [5] Set Items Is Unique
# -----------------------------

Test_set = {1, "Ahmed", 85.5}
print(Test_set)
# print(Test_set[1])
# print(Test_set[1::])


Test_set = {1, "Ahmed", 85.5, (5, "test")}
print(Test_set)

# Test_set = {1,"Ahmed",85.5,[5,"test"]}  unhashable type: 'list'
# print(Test_set)


Test_set = {1, 1, "Ahmed", 85.5, (5, "test")}
print(Test_set)

# -----------------
# -- Set Methods --
# -----------------


# clear() => بتعمل ازاله لكل العناصر
a = {1, 2, 3}
a.clear()
print(a)

print("-" * 40)

# union()   => اتحاد لمجموعتين (a | b)
b = {1, 2, 3, 5}
c = {4, 5}
b.union(c)
print(b | c)
print(b.union(c))


# add() Added one item
b = {1, 2, 3, 5}
b.add(6)
print(b)

# copy()  Copied from set
d = {1, 2, 3, 5}
e = d.copy()
print(e)


# remove() remove specific item
g = {1, 2, 3, 4}
g.remove(1)
# g.remove(7)
print(g)

# discard() => error انها مش بترجع رساله  remove بتعمل ازاله لعنصر معين بس بتختلف عن
h = {1, 2, 3, 4}
h.discard(5)
print(h)
h.discard(50)
print(h)


# pop() Return number and remove  =>  لاخر حاجه اتضافت return في الداتا ستركشر المفروض انها بتعمل
i = {"A", 0, True, 1, 2, 3, 4, 5}
print(i.pop())
print(i.pop())
print(i.pop())

test_list = [1, 5, 87, 898]
print(test_list.pop())

# update() == unoin()  بتعمل دمج للمجموعات و بتشيل المتكرر

j = {1, 2, 3}
k = {1, "A", "B", 2}
j.update(k)
print(j)

print("-" * 40)  # Separator


# -----------------
# -- Set Methods --
# -----------------

# difference = ( - )
# union = ( | )
# intersection ( & )
# symmatric_difference ( ^ )


# difference() =>  (A - B)
a = {1, 2, 3, 4}
b = {1, 2, 3, "Osama", "Ahmed"}
print(a.difference(b))
print(a - b)
print(b.difference(a))
print("-" * 40)  # Separator


# difference_update() => orginal set  بس  بتنقل التحديثات   difference هي نفس
c = {1, 2, 3, 4}
d = {1, 2, "Osama", "Ahmed"}
print(c)
c.difference_update(d)  # (c - d)
print(c)
print("-" * 40)  # Separator


# intersection()  => المشترك بين المجموعتين   (A ∩ B)  =>  (e & f)
e = {1, 2, 3, 4, "X", "Osama"}
f = {"Osama", "X", 2}
print(e)
print(e.intersection(f))
print(e & f)

print("-" * 40)  # Separator

# intersection_update()  =>    فيها الداتا الجديده  original set  المشترك بين المجموعتين  بس بتخلي  (A ∩ B)  =>  (e & f)
e = {1, 2, 3, 4, "X", "Osama"}
f = {"Osama", "X", 2}
print(e)
e.intersection_update(f)
print(e)

print("-" * 40)  # Separator

# symmetric_difference() => A Δ B = (A ∪ B) - (A ∩ B)  => اللي مش موجود في الاتنين  =>  (i ^ j)
i = {1, 2, 3, 4, 5, "X"}
j = {"Osama", "Zero", 1, 2, 4, "X"}

print(i.symmetric_difference(j))

print("-" * 40)  # Separator


# symmetric_difference_update()    =>  original set بتنقل الشغل الجديد في  =>  (i ^ j)
i = {1, 2, 3, 4, 5, "X"}
j = {"Osama", "Zero", 1, 2, 4, "X"}
print(i)
i.symmetric_difference_update(j)
print(i)
s = i ^ j
print(s)


print("-" * 40)  # Separator


# -----------------
# -- Set Methods --
# -----------------

# issuperset() =>  method returns True if all items in the specified set exists in the original set, otherwise it retuns False.


a = {1, 2, 3, 4}
b = {1, 2, 3}
c = {1, 2, 3, 4}
print(a.issuperset(b))
print(b.issuperset(a))
print(a.issuperset(c))


print("-" * 40)  # Separator

# issubset() Return method returns True if all items in the set exists in the specified set, otherwise it retuns False.

x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}

z = x.issubset(y)

print(z)

print("-" * 40)  # Separator

# isdisjoint() method returns True if none of the items are present in both sets, otherwise it returns False. => return true لو مكنش  return false لو بينهم حاجه مشتركه
h = {1, 2, 3}
g = {1, 2, 3, 4}
i = {10, 11, 12}

j = h.isdisjoint(g)
print(j)

d = h.isdisjoint(i)
print(d)

print("-" * 40)  # Separator


# ---------------------------
# -- Dictionary --
# ----------------
# [1] Dict Items Are Enclosed in Curly Braces
# [2] Dict Items Are Contains Key : Value
# [3] Dict Key Need To Be Immutable => (Number, String, Tuple) List Not Allowed
# [4] Dict Value Can Have Any Data Types
# [5] Dict Key Need To Be Unique  => لو كررت نفس القيم هياخد اخر قيمه
# [6] Dict Is Not Ordered You Access Its Element With Key
# ----------------------------

# Syntax
Dict = {"Key": "value"}

dict = {
    "name": "ahmed",
    "age": 20,
    "gpa": 3.23,
    "age": 21,
    "tuple": (1, 3, "test")
}

print(dict)
# keys => return all keys in dictionary
print(dict.keys())

# keys => return all values in dictionary
print(dict.values())

# get() => return specific iems from dictionary
print(dict.get("age"))  # =>  print(dict["age"])


print("-" * 40)  # Separatorprint("-" * 40)  # Separator


# Two-Dimensional Dictionary  =>  dict يحتوي علي  dict   =>  [][]

Two_Dimensional = {
    "name": {
        "name_1": "ahmed",
        "name_2": "ali",
        "name_3": "ammar",
        "name_4": "faris"
    },
    "age": {
        "age_1": 20,
        "age_2": 22,
        "age_3": 28,
        "age_4": 22,
    },
    "gpa": {
        "gpa_1": 3.2,
        "gpa_2": 3.42,
        "gpa_3": 3.57,
        "gpa_4": 3.0,
    },
}

print(Two_Dimensional)
print(Two_Dimensional.keys())
print(Two_Dimensional.values())

print("-" * 40)  # Separatorprint("-" * 40)  # Separator

# one dict
print(Two_Dimensional.get("age"))
print(Two_Dimensional["gpa"])

# Two Dimensional
print(Two_Dimensional["age"]["age_2"])
print(Two_Dimensional["gpa"]["gpa_2"])

print("-" * 40)  # Separatorprint("-" * 40)  # Separator

# Dictionary Length  => len() => return lenght dict

print(len(Two_Dimensional))
print(len(Two_Dimensional["age"]))


# Create Dictionary From Variables

frameworkOne = {
    "name": "Vuejs",
    "progress": "80%"
}

frameworkTwo = {
    "name": "ReactJs",
    "progress": "80%"
}

frameworkThree = {
    "name": "Angular",
    "progress": "80%"
}

framework = {

    "one": frameworkOne,
    "Two": frameworkTwo,
    "Three": frameworkThree,

}


print(framework)

# ------------------------
# -- Dictionary Methods --
# ------------------------

# clear() =>  Remove all items from dictionary

framework = {

    "one": frameworkOne,
    "Two": frameworkTwo,
    "Three": frameworkThree,

}

framework.clear()
print(framework)


print("-" * 40)

# update()

member = {
    "name": "Osama"
}
print(member)
member["age"] = 36
print(member)

# member.update({"country": "Egypt"})
# print(member)


print("-" * 50)

# copy()

main = {
    "name": "Osama"
}

c = main.copy()
print(c)

# keys() + values()

framework = {

    "one": frameworkOne,
    "Two": frameworkTwo,
    "Three": frameworkThree,

}

print(framework.keys())
print(framework.values())


# ------------------------
# -- Dictionary Methods --
# ------------------------

print("-" * 50)

# setdefault("key" , "value") => return value

test = {
    "name": "ahmed",
    "phone": 1017363740
}
print(test)
print(test.setdefault("name"))
print(test)
print("=" * 50)

# popitem()  =>  dict بترجع اخر قيمه انضافت في

test = {
    "name": "ahmed",
    "phone": 1017363740
}

# add new key (1)

test["gpa"] = 3.2
print(test)

# add new key (2)

test.update({"age": 20})
print(test)


print(test.popitem())


# items() return all items from dict

test = {
    "name": "ahmed",
    "phone": 1017363740,
    "age": 20
}


test_items = test.items()

test["gpa"] = 2.9

print(test_items)


# fromkeys() => create dict from two variable

a = ("k1", "k2", "k3")
b = ("v1")
print(dict.fromkeys(a, b))


List = [11, 78, 7, 1, 2, 3, 4, 5, 6, 6]
List.remove(6)
List.sort(reverse=True)
print(List)

List = [11, 78, 7, 1, 2, 3, 4, 5, 6, 6]
List.reverse()
print(List)


List = [11, 78, 7, 1, 2, 3, 4, 5, 6, 6]
List_copy = List.copy()
print(List_copy)

g = [1, 2, 3, 4, 5, "A", "B"]
g.pop()
print(g)


# ----------------------
# -- Boolean   => منطقي
# ----------------------
# [1] In Programming You Need to Known Your If Your Code Output is True Or False
# [2] Boolean Values Are The Two Constant Objects False + True.
# ---------------------------------------------------------------


S = " "
print(S.isspace())

print(10 > 1)
print(10 > 10)
print(10 > 100)

print("=" * 50)


# bool() => true || false
print(bool("ahmed"))
print(bool(True))
print(bool(1))
print(bool(1.588))

print("=" * 50)

print(bool())
print(bool(0))
print(bool(None))
print(bool({}))
print(bool(()))
print(bool([]))
print(bool(""))
print(bool(''))

print("=" * 50)

# -----------------------
# -- Boolean Operators --
# -----------------------
# and  لازم كل الشروط تتحقق
# or لازم شرط واحد ع الاقل يتحقق
# not بتفي الشرط  =>  not true || false
# -----------------------


age = 20
name = "ahmed"
print(age == 20 and name == "ahmed")
print(age < 20 or name == "ahmed")
print(not age == 20)

print("=" * 50)


# --------------------------
# -- Assignment Operators --
# --------------------------
# =
# +=
# -=
# *=
# /=
# **=
# %=
# //=
# --------------------------

a = 5
b = 10
c = a + b
print(c)

# var_1 = self [operator (+,-,/,*,%,**,//)] + var_2
# a = a + b

# var_1 [operator  (+,-,/,*,%,**,//)] = var_2
a += b
print(a)


d = 15
e = 3
d -= e
print(d)

d /= e
print(d)

d *= e
print(d)

d //= e
print(d)

d %= e
print(d)


print("=" * 50)

# --------------------------
# -- Comparison Operators --
# --------------------------
# [ == ] Equal
# [ != ] Not Equal
# [ > ] Greater Than
# [ < ] Less Than
# [ >= ] Greater Than Or Equal
# [ <= ] Less Than Or Equal
# --------------------------


a = 5
print(a == 5)
print(a == 5.00)
print(a != 5)
print(a > 4)
print(a >= 5)
print(a < 5)
print(a <= 5)


# ---------------------
# -- Type Conversion --
# ----------------------

# str()  int => string


a = 6
print(type(a))
print(type(str(a)))

print("#" * 50)


# tuple()

S = "TAHA"
L = [1, 3, 9, 89]
s = {1, 2, 3, 4, 5, "ahmed"}
d = {
    "name": "ahmed",
    "age": 20
}

print(tuple(S))
print(tuple(s))
print(tuple(L))
print(tuple(d))

print("#" * 50)


# list()

S = "TAHA"
L = (1, 3, 9, 89)
s = {1, 2, 3, 4, 5, "ahmed"}
d = {
    "name": "ahmed",
    "age": 20
}

print(list(S))
print(list(s))
print(list(L))
print(list(d))


print("#" * 50)

# set()

S = "TAHA"
L = (1, 3, 9, 89)
s = [1, 2, 3, 4, 5, "ahmed"]
d = {
    "name": "ahmed",
    "age": 20

}

print(set(S))
print(set(s))
print(set(L))
print(set(d))


# dict("keys" : "values")


S = "TAHA"
L = (1, 3, 9, 89)
s = [1, 2, 3, 4, 5, "ahmed"]
d = {
    "name": "ahmed",
    "age": 20

}

print(set(S))
print(set(s))
print(set(L))
print(set(d))
#  -------------------------------
#  Information About File
#  License
#  Who Created The File
#  When The File Created
#  Why The File Created
#  Write Beside The Programming Line
#  Write Before The Programming Line
#  Prevent Code From Run
#  -------------------------------


print("I Love Python")  # This is Inline Comment
print("Programming")  # I Used This Method Because of Bla Bla Bla
print("Programming")  # If You Used Test Method Will Through Error


# this is not comment
"""
This is
Not
Multiple
Line
Comments
"""

#  ----------------------------
#  type()
#  All Data in Python is Object
#  ----------------------------

print(type(10))  # int => Integer
print(type(100))  # int => Integer
print(type(-50))  # int => Integer

print(type(100.9))  # float => Floating Point Number
print(type(1.0950950))  # float => Floating Point Number
print(type(-100.9595))  # float => Floating Point Number

print(type("Hello Python"))  # str => String

print(type([1, 2, 3, 4, 5]))  # list => List

print(type((1, 2, 3, 4, 5)))  # tuple => Tuple

print(type({"One": 1, "Two": 2, "Three": 3}))  # dict => Dictionary

print(type(2 == 20))  # bool => Boolean


# ---------------------
# -- Type Conversion --
# ----------------------

# str()  int => string


a = 6
print(type(a))
print(type(str(a)))

print("#" * 50)


# tuple()

S = "TAHA"
L = [1, 3, 9, 89]
s = {1, 2, 3, 4, 5, "ahmed"}
d = {
    "name": "ahmed",
    "age": 20
}

print(tuple(S))
print(tuple(s))
print(tuple(L))
print(tuple(d))

print("#" * 50)


# list()

S = "TAHA"
L = (1, 3, 9, 89)
s = {1, 2, 3, 4, 5, "ahmed"}
d = {
    "name": "ahmed",
    "age": 20
}

print(list(S))
print(list(s))
print(list(L))
print(list(d))


print("#" * 50)

# set()

S = "TAHA"
L = (1, 3, 9, 89)
s = [1, 2, 3, 4, 5, "ahmed"]
d = {
    "name": "ahmed",
    "age": 20

}

print(set(S))
print(set(s))
print(set(L))
print(set(d))

# dict()
# (1) string  =>   dict ل  string مينفعش احول من
# (2) tuple   =>    nested tuple  لازم يكون في
# (3) list    =>     nested list  لازم يكون في
# (4)  set    =>   dict ل  set مينفعش احول من   unhashable

# d = (("A", 1), ("B", 2), ("C", 3))  # Tuple
# e = [["One", 1], ["Two", 2], ["Three", 3]]  # List
# print(dict(d))
# print(dict(e))


# ----------------
# -- User Input --
# ---------------

# First_Name  = input("what is  the first name ?")
# Middle_Name = input("what is  the middle name ?")
# Last_Name   = input("what is  the last name ?")

# First_Name = First_Name.capitalize().strip()
# Middle_Name = Middle_Name.capitalize().strip()
# Last_Name = Last_Name.capitalize().strip()


# print(f"Welcome , {First_Name} {Middle_Name:.1s} {Last_Name}")


# ---------------------------
# -- Practical Slice Email --
# ---------------------------

print("*" * 50)

# Email = "ahmedtaha8963@gmail.com"
# print(Email[0:Email.index("@")])
# print(Email[Email.index("@"):])

# print("*" * 50)

# UserName = input("what`s your name ?").strip().capitalize()
# Email    = input("what is your email ?").strip()
# print(f"UserName: {UserName}  and u Email : ({Email})")
# print(Email[Email.index("@") + 1 :  ])


# Age calc

Age = int(input("Enter Your Age ?"))

Months = Age * 12
Weeks = Months * 4
Days = Age * 365
Hours = Days * 24
Minutes = Hours * 60
Seconds = Minutes * 60

print(f"Your Age : {Age}  , Months : {Months} , Weeks : {Weeks} , Days : {Days:,} , Hours : {Hours:,} , Minutes : {Minutes:,}, Seconds : {Seconds:,}")

# Enter Your Age ? 20
# Your Age : 20  , Months : 240 , Weeks : 960 , Days : 7,300 , Hours : 175,200 , Minutes : 10,512,000, Seconds : 630,720,000


# --------------------
# --  Control Flow  --
# -- If, Elif, Else --
# -- Make Decisions --
# --------------------


# Gpa = float(input("Enter your gpa : "))
# if Gpa >= 2 and Gpa <= 2.5 :
#   print("Great your Grade : C ")
# else :
#  print("Great your Grade : C+ ")

# ---------------
# -- Nested If --
# ---------------


UserName = input("Enter Your User Name: ")
Age = int(input("Enter your Age : "))
Gpa = float(input("Enter Your Gpa : "))
Id = int(input("Enter your id : "))
Status = input("Enter Your User Status: ")

if Status == "frech":
    if Gpa >= 3.6:
        print(f"Your name :{UserName} , id :{Id} and your grade : A+")
        
        
        # ممكن اكتب الشرط و النتيجه في سطر واحد
    if Gpa >= 3.6 : print(f"Your name :{UserName} , id :{Id} and your grade : A+")

# ----------------------------------
# -- Ternary Conditional Operator --
# ----------------------------------


# Short If
print(f"Your name :{UserName} , id :{Id} and your grade : A+ " if Gpa >= 3.6 else "Movie S Good 4U And Happy Watching")
# Condition If True | If Condition | Else | Condition If False




# -------------------------------------------------
# -- Calculate Age Advanced Version and Training --
# -------------------------------------------------

# Write A Very Beautiful Note
print("#" * 80)
print(" You Can Write The First Letter Or Full Name of The Time Unit ".center(80, '#'))
print("#" * 80)

# Collect Age Data
age = input("Please Write Your Age").strip()

# Collect Time Unit Data
unit = input("Please Choose Time Unit: Months, Weeks, Days ").strip().lower()

# Get Time Units
months = int(age) * 12
weeks = months * 4
days = int(age) * 365

if unit == 'months' or unit == 'm':

  print("You Choosed The Unit Months")
  print(f"You Lived For {months:,} Months.")

elif unit == 'weeks' or unit == 'w':

  print("You Choosed The Unit Weeks")
  print(f"You Lived For {weeks:,} Weeks.")

elif unit == 'days' or unit == 'd':

  print("You Choosed The Unit Days")
  print(f"You Lived For {days:,} Days.")




# ----------------------------------
# -- Practical Membership Control --
# ----------------------------------


Students = ["ahmed","ali","ammar","alaa","kareem","ashraf","eslam"]
Name = input("Please enter your name: ").strip().lower()

if Name in Students :
    print(f"Welcome ,{Name} you are rejestered in system")
    print("Done, you are rejester.")
    option = input("Do you intend to attend").strip().lower()
    if option == "yes" or  option == "y" :
        print("Thanks")
    else:
       print("sorry ") 
        
else :
 print("sorry you aren`t rejestration is ")
 New_Student = input("enter your name to registration in system").strip().lower()
 Students[Students.append(New_Student)] = New_Student
 print("Done, you are rejester.")
 print(Students)



# -------------------
# -- Loop => While --
# -------------------
# while condition_is_true
#   Code Will Run Until Condition Become False
# -----------------------


a = 8 
while (a<15) :
    print(a)
    
    a+=1
    
    
v = 2
while v > 0 and v < 1000:
    print(v)
    v *= 2


# ----------------------------
# -- Loop => While Training --
# ----------------------------
# while condition_is_true
#   Code Will Run Until Condition Become False
# -----------------------

myF = ["Os", "Ah", "Ga", "Al", "Ra", "Sa", "Ta", "Ma", "Mo", "Wa"]
a = 0 
while a < len(myF) :
    print(f'{str(a+1).zfill}- {myF[a]}')
    a +=1 
    
    
# favorite subject

favorite_subject = 5
subject = []

while favorite_subject > 0:
  s = input("Enter  your favorite subject: ").strip().lower()
  subject.append(s)
  favorite_subject -= 1
  print("favorite subject added.")
  print(subject)
  print(f" you can add {favorite_subject} subject.")

else:
    print("Sorry you can`t added new subject")

b = 0
while b < len(subject):
   print(subject[b])
   b += 1
   
   
# ----------------------------
# -- Loop => While Training --
# -- Simple Password Guess --
# ----------------------------



password = "ahmed89@"
tries = 5
enter_pass = input("please enter your password ")

while enter_pass != password:
    tries -= 1
    print(f"Wrong Password, { 'Last' if tries == 0 else tries } Chance Left")
    enter_pass = input("please enter your password ")
    if tries == 0:
        print("Sorry , you use  all tries.")
        break
else:
    print("Password correct")


print("loop")
