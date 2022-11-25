# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

number = float(input('Введите число '))

number = str(number)
summa = 0

for i in range(len(number)):
    if number[i] != ".":
        summa += int(number[i])


print(f'Сумма чисел равна {summa}')
