#a = (v - v0)/t

def main():
	
	def ускорение(a = "none", v = "none", v0 = "none", t = "none"):
			
			все_переменные = [a, v,v0,t]
			известные = []
			неизвестные = []	
			for i in все_переменные:
				if i == "none":
					неизвестные.append(i)
				else:
					известные.append(i)				
			print(f"известные переменные: {известные}\nнеизвестные переменные: {неизвестные}")
			if a == "none":
				return (v-v0)/t
	
	func = input()
	print(eval(func))
	
	main()
main()	
