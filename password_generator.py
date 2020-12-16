import random
import sys

char = ["A","B","C","D","E","F","G","H","I","J","K",
		"L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

def generate(num):
	result = ""
	for i in range(num):
		s = "".join(random.choices(char,k=6))
		result += f"{s}\n"
	return result.strip("\n")

def create_file(result):
	with open("pseudo_password.txt","w") as f:
		f.write(result)

def main(num):
	result = generate(num)
	create_file(result)

if __name__ == "__main__":
	main(int(sys.argv[1]))