from colorama import Fore, Back, Style
import os
type1 = type(a)
type2 = type(b)
while True:
    os.system("clear")
    print(Fore.BLUE + "дЭбылный кулькулятор v1")
    print("")
    a = input("Введите первое число: ")
    if type1 == str:
        print("Попробуй ещё раз, видимо у тебя была буква в числе")
    b = input("Введите второе число: ")
    print("")
    d = input("Что вы хотите сделать? +, -, *, /")
    if d == "+":
        c = a + b
    elif d == "-":
        c = a - b

    print("Ответ:", c)
print(Fore.RESET + "")

