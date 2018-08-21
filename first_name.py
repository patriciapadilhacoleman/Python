first_name = "patricia"
last_name = "coleman"

print("Good Morning,  " + first_name.title() + " !")

famous_person = "  Shakespeare      "
print(famous_person.rstrip())
print(famous_person.strip())
print(famous_person.lstrip())
message = famous_person.title() + ' said: "To Be or Not To Be"'
print(message)

#working w integers
print(str(2 * 2 + 4))

print(str(32 / 4))

#working with lists

names = ["patricia", "joana", "stephanie", "marisa", "bruna"]
print(names)
names[0] = "joana"
print(names)
names.append("leo")
print(names)
names.insert(10, "simone")
print(names)
del names[-1]
print(names)
popped_name = names.pop()
print(popped_name)
names.remove("joana")
print(names)
names.sort()
print(names)