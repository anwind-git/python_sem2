# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

n = int(input('Введите число: '))

summa = 0
array = []

for i in range(1, n + 1):
    num = round((1 + 1 / i)**i, 2)
    array.append(f"{i}: {num}")
    summa += num

print(array)
print(f"Сумма последовательности чисел: {summa}")

