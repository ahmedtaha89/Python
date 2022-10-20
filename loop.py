# from re import split, sub

import re
# string = "My Name-Ahmed Taha"
# split = re.split(r"\s|-",string,2)
# print(split)


# # sub = replace 
# print(sub(r"\s",r"\t ","My Name Ahmed Taha",2))


# ------------------------------------------------------
# -- Regular Expressions => Group Trainings And Flags --
# ------------------------------------------------------

import re

my_web = "https://www.elzero.org:8080/category.php?article=105?name=how-to-do"

search = re.search(r"(https?)://(www)?\.?(\w+)\.(\w+):?(\d+)?/?(.+)", my_web)

print(search.group())
print(search.groups())

for group in search.groups():

  print(group)

print(f"Protocol: {search.group(1)}")
print(f"Sub Domain: {search.group(2)}")
print(f"Domain Name: {search.group(3)}")
print(f"Top Level Domain: {search.group(4)}")
print(f"Port: {search.group(5)}")
print(f"Query String: {search.group(6)}")