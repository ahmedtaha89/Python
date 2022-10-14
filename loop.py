
def reverse_string(my_string):
  for str in my_string[-1::-1]:
    yield str

# Reverse The String
for c in reverse_string("Elzero"):
  print(c)
