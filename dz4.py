# Задайте список из N элементов, заполненных числами из промежутка[-N, N]. Найдите
# произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
# Реализуйте алгоритм перемешивания списка.

from random import Random, randint


N = int(input("Введите число: "))
array = []
for i in range(N):
    array.append(randint(-N, N))

print(array)

summa = 1
position = 0

f = open('file.txt', 'w')

while position < len(array):
    position = int(input("Введите № позиции: "))
    if position < len(array):
        summa *= array[position]
        f.write(str(position) + "\n")
    else:
        print(f"Позиция: {position} не существует.")
        print(f"Произведение элементов на указанных позициях: {summa}")

f.close()