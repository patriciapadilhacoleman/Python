subscriber = {'first_Name' : 'Patricia', 'last_Name' : 'Padilha', 'phone' : '310-658-3071'}

children_bdate = {
	'Kyle':'04/15/93',
	'Melissa': '05/19/94',
	'Lucas': '07/28/04',
}

children = []

#create a chilldren's dictionary
for children_number in range(6):
	new_child = {'name': 'Anna', 'gender' : 'f', 'schools' : ['Chadwick','Lunada Bay','RHCD']}
	children.append(new_child)


print(children)
print("# of children is " + str(len(children)))


for school in children[1]['schools']:
		print("\t" + school)

print("Today's b-day is:", children_bdate['Kyle'])

subscriber['zip_code'] = '90274'
subscriber['city'] = 'Palos Verdes Estates'

if subscriber['zip_code'] == '90274':
	print("You live in PVE")
elif subscriber['zip_code'] == '90275':
	print("You live in RPV")
else:
	print("I don't know where you live")

for key, value in subscriber.items():
	print(value + "\t")

if 'Jonas' not in children_bdate.keys():
	children_bdate['Jonas'] = '03/05/07'


for child in sorted(children_bdate.keys()):
	print(child)

