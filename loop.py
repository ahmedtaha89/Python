my_tuble = ("ahmed","taha","ahmed","ahmed89")

for t in my_tuble:
    print(t,end=" - ")

print("-" * 40)

ITER = iter(my_tuble)

print(next(ITER))
print(next(ITER))
print(next(ITER))