#a = (v - v0)/t
print("Добро пожаловать в Era!\n")


def main():	
	func = input()+"()"

	def znach(x):
		x = x.replace(" ", "")
		a = x.split("=")
		return a
	
	def ускорение(): 
		print("Напишите известные вам значения, Например\nv0 = 20, v = 40, t = 4\n")
		ra = input()
		a = "none"
		v = "none"
		v0 = "none"
		t = "none"
		result = 0
		
		prim = ra.split(",")
		for i in prim:
			k = znach(i)
			if k[0] == "a":
				a = int(k[1])
			elif k[0] == "v":
				v = int(k[1])
			elif k[0] == "v0":
				v0 = int(k[1])
			elif k[0] == "t":
				t = int(k[1])
		print(f"a = {a}, v = {v}, v0 = {v0}, t = {t}")
		
		if a == "none":
			print( f"\nНаходим ускорение по формуле: \na = (v - v0)/t\na = ({v} - {v0})/{t}")
			result = (v - v0)/t
			print(f"\na = {result}")
		
		elif t == "none":
			print( f"\nНаходим ускорение по формуле: \na = (v - v0)/t\na = ({v} - {v0})/{t}")
			result = (v - v0)/a
			print(f"\nt = {result}")
			
		elif v == "none":	
			print( f"\nНаходим ускорение по формуле: \na = (v - v0)/t\na = ({v} - {v0})/{t}")
			result = a*t
			print(f"\nv - v0 = {result}")
			result = result -v0
			print(f"\nv = {result}")
		
		elif v0 == "none":	
			print( f"\nНаходим ускорение по формуле: \na = (v - v0)/t\na = ({v} - {v0})/{t}")
			result = a*t
			print(f"\nv - v0 = {result}")
			result = v - result
			print(f"\nv0 = {result}")
			
	eval(func)
	main()
main()
				
		
		