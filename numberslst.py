#working with numbers

numbers = list(range(0,100,2))
print(numbers)

squares = []
for value in range(1,10):
	square = value * value
	squares.append(square)
	
print(squares)

uptomil =[ value for value in range(1,1000000)]
print(min(uptomil))
print(max(uptomil))
print(sum(uptomil))

odd_numbers =[value for value in range(1,21,2)]
print(odd_numbers)

mult_three = [value * 3 for value in range(1,31)]
print(mult_three)