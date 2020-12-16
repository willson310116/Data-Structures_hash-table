with open("hash_value.txt") as f:
	data = f.read()

data = data.split("\n")[:-1]

# arrange as table(dict) to search password by hash value
# table = {hash_value:[salt,password],...}

table = {}
for i in range(len(data)):
	items = data[i].split(" ")
	password, salt, hash_value = items[0],items[1],items[2]
	table[hash_value] = [salt,password]

val = input("search for a hash value, q for quit\n> ")
while val != "q":
	if val in table.keys():
		print(f"recovered password: {table[val][1]}\nsalt value: {table[val][0]}")
	else:
		print("No match is found!")
	val = input("search for a hash value, q for quit\n> ")
