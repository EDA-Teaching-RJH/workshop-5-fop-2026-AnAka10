Name = input ("CamelCase: ")
Snake_Case = ""
for char in Name:
    if char.isupper():
        Snake_Case += "_" + char.lower()
    else:
        Snake_Case += char
print ("Snake_Case:", Snake_Case)