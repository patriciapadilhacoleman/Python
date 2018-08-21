
available_toppings = ['olives','anchovies','pineapple','mushrooms','green peppers','extra cheese', 'chicken']

requested_toppings = ['french fries','green peppers','extra cheese', 'chicken']

#requested_toppings = []

#if requested_toppings:

for requested_topping in requested_toppings:

	if requested_topping in available_toppings:
		
		print("adding " + requested_topping + "...")
		
	else:
		
		print("Sorry, we don't have " + requested_topping + "...")

print("\nFinished making your pizza!")

#else:
#	print("Are you sure you want a plain pizza?")