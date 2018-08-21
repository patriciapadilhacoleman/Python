
people = []


person = {
'first_name' : 'Rogerio',
'last_name':'Ruella', 
'city':'Niteroi',
'age': '47'
}

for person in range(30) :
	new_person


for key, value in person.items():
	print("\nKey: " + key)
	print("\tValue: " + str(value))
# print(person['first_name'])
# print(person['last_name'])
# print(person['city'])
# print(person['age'])print(person[first_name])

favorite_color = {
	'Jen' : 'white',
	'Tom' : 'blue',
	'Cindy' : 'red',
	'Elle' : 'pink',
	'John' : 'black',
	'Dennis': 'red',
	'George': 'blue'
}

for name, color in favorite_color.items():
	print(name.title() + " likes " + color.title() + ".")

for name in favorite_color.keys():
	print(name.title())
	
if 'Betty' not in favorite_color.keys():
	print("What's your favorite color, Betty?")

for name, color in sorted(favorite_color.items()): 
	print(name.title() + " likes " + color.title() + ".")

#unique colors - NO repeats
for colors in set(sorted(favorite_color.values())):
	print(colors)