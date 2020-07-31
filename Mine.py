from colorama import Fore, Back, Style
import os
os.system("clear")
print(Fore.BLUE + "дЭбылный кулькулятор v1")
print("")
i = 0
while i < 10:
	while True:
		try:
			a = float(input("Введите первое число: "))
			break
		except ValueError:
			print("Попробуй ещё раз, видимо у тебя была буква в числе")
	while True:
			try:
				b = float(input("Введите второе число: "))
				break
			except ValueError:
				print("Попробуй ещё раз, видимо у тебя была буква в числе")
	while True:
			d = input("Что ты хочешь сделать? +, -, *, /: ")
			try:
				if d == "+":
					c = a + b
					break
				elif d == "-":
					c = a - b
					break
				elif d == "*":
					c = a * b
					break
				elif d == "/":
					c = a / b
					break
				else:
					print("Ты невернно ввёл действие, попробуй ещё раз")
					continue
			except ZeroDivisionError:
				print("Дружище, на 0 делить нельзя, попробуй ещё раз")
				continue
	while True:
				print("Ответ:", c)
				break
	while i < 10:
				m = input(("Хотите ещё раз? Да или нет: "))
				if m == "Нет":
					print(Fore.RESET)
					i = 11
				elif m == "Да":
					os.system("clear")
					break
