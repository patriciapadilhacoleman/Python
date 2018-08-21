users = {
	'01': {
	'nome': 'Pedro',
	'sobrenome': 'Alvarez',
	'cidade': 'Campos',
	},
	'02': {
	'nome': 'Paula',
	'sobrenome': 'Alvarez',
	'cidade': 'Caxias',
	},
	'03': {
	'nome': 'Paulo',
	'sobrenome': 'Silva',
	'cidade': 'Campos',
	},
	'04': {
	'nome': 'Paula',
	'sobrenome': 'Almeida',
	'cidade': 'Campos',
	},
	'05': {
	'nome': 'Pedro',
	'sobrenome': 'Ortega',
	'cidade': 'Niteroi',
	},
}

fname = input("Enter your first name: ")
lname = input("Enter your last name: ")
city = input("Enter your city: ")

users ['0' + str(len(users) + 1)] = {
	'nome': fname.title(),
	'sobrenome': lname.title(),
	'cidade': city.title(),
	}
}

#users.append(new_user
users.append(new_user)

print(new_user)

for key, info in users.items():
	print(key + "\t Nome: " + info['nome'] + " " + info['sobrenome'])
	print("\t Cidade: " + info['cidade'] + "\n")