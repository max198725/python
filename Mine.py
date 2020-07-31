from colorama import Fore, Back, Style
import os
while True:
    os.system("clear")
    print(Fore.BLUE + "дЭбылный кулькулятор v1")
    print("")
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    print("")
    d = input("Что вы хотите сделать? +, -, *, /")
    if d == "+":
        c = a + b
    elif d == "-":
        c = a - b

    print("Ответ:", c)
print(Fore.RESET + "")

