places = ["italia","grecia","patagonia","russia","croacia"]

print(places)

print(sorted(places))

print(places)

print(sorted(places, reverse = True))

print(places)

places.reverse()

print(places)

places.reverse()

print(places)

places.sort()

print(places)

for place in places:
	print(" I want to visit " + place.title())

print("I must save money")

print("The first three places I would like to visit are: " + str(places[0:3]))

print("The first three places I would like to visit are: " + str(places[1:4]))

print("The last three places I would like to visit are: " + str(places[-3:]))

rog_places = places[:]

print(rog_places)

rog_places.append("maldivas")

for rog_place in rog_places:
	print(rog_place)
