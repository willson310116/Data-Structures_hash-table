with open("password.txt") as f:
	data = f.read()

data = data.split("\n")[:-2]

res = []
for i in range(len(data)):
	asc = [str(ord(data[i][n])) for n in range(len(data[i]))]
	password = "".join(asc)
	res.append(password)
table = {}

for i in range(len(res)):
	temp = []
	for j in range(1000):
		temp.append(f"{j:03}"+res[i])
	table[res[i]] = temp

def hash(asc):
	left = int(asc[:8])
	right = int(asc[8:])
	return ((243 * left) + right)%85767489

for key in table:
	for i in range(len(table[key])):
		table[key][i] = {table[key][i]:hash(table[key][i])}

# data structure(table act as hash table)
# table: dict -> key:asc (str), value: [{},{}...{}] (list)
# item in value: dict -> key: asc+salt (str), value: hash value (int)

# search hash value:
# 1. password -> ascii code
# 2. ascii code add salt at the front
# 3. derive hash value using hash function

result = ""
for asc in table:
	temp = [int(asc[i:i+2]) for i in range(0,len(asc),2)]
	asc_str = "".join(map(chr,temp)) # convert ascii code to original string
	for i in range(len(table[asc])):
		for salt in table[asc][i]:
			result += f"{asc_str} {salt[:3]} {table[asc][i][salt]}\n"
		

with open("hash_value.txt","w") as f:
	f.write(result)
