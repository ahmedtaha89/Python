myTexts = ["Osama", "Omer", "Omar", "Ahmed", "Sayed", "Othman"]
def check_name(name):
    return name.endswith("d")

check =filter(check_name,myTexts)
for c in check:
    print(c)

print("-" * 40)

for NAME in filter(lambda name : name.startswith("O"),myTexts):
    print(NAME)
    