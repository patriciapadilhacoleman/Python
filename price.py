age = 3

if age < 5 :

	admission = 5

elif age < 19 and age >= 5 :
	
	admission = 10

elif age > 18 and  age < 65 :

	admission = 15

else:

	admission = 7


print("Your admission price is $ " + str(admission) + " dollars!")