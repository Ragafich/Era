print("Добро пожаловать в Era! \n")

print("Если вы не знаете доступных команд, напишите \"помощь\" \nв командную строку\n")
def main():
	def помощь():
		
		print("Напишите, что вам необходимо найти")
		print("Например, \n площадь\n")
		print("\nЧисло π в данной программе равно 3.14/n")
		print("Список доступных на данный момент функций: \n площадь \n периметр \nСписок доступных фигур: \n квадрат \n прямоугольник \n круг")
	
	def площадь():
		print("напишите название фигуры, площадь которой необходимо найти")
		figure = input()
		while " " in figure:
			figure = figure.replace(" ", "")
			
		if figure == "круг":
			print("напишите радиус круга")
			r = int(input())
			result = 3.14*(r**2)
			return f"площадь круга с радиусом {r} равен {result}"
			
		elif figure == "квадрат":
			print("напишите длину стороны квадрата")
			a = int(input())
			result = a**2
			return f"площадь квадрата со стороной {a} равна {result}"
			
		elif figure == "прямоугольник":
			print("напишите длины его сторон через пробел")
			a,b= input().split(" ")
			result = int(a)*int(b)
			return f"площадь прямоугольника со сторонами {a} и {b} равна {result}"
		else:
			print("извините, мы пока думаем над этим")	
	
	def периметр():
		print("напишите название фигуры, периметр которой необходимо найти")
		figure = input()
		
		while " " in figure:
			figure = figure.replace(" ", "")
		
		if figure == "круг":
			print("напишите радиус круга")
			r = int(input())
			result = 3.14*r*2
			return f"площадь круга с радиусом {r} равен {result}"
			
		elif figure == "квадрат":
			print("напишите длину стороны квадрата")
			a = int(input())
			result = a*4
			return f"периметр квадрата со стороной {a} равен {result}"
			
		elif figure == "прямоугольник":
			print("напишите длины его сторон через пробел")
			a,b= input().split(" ")
			result = (int(a)+int(b))*2
			return f"периметр прямоугольника со сторонами {a} и {b} равна {result}"
	
		else:
			print("извините, мы пока думаем над этим")
	print()
	func = str(input()) + "()"
	
	while " " in func:
		func = func.replace(" ", "")
		
	print(eval(func))
	main()
main()