# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K – положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

# Метод №1 через while

"""""
list = [1, 2, 3, 4, 5]

number = int(input('Введите число, на которое сдвинем массив: '))
i = 0
while i < number:
    list.insert(0, list[len(list) - 1])   # последний индекс вставляем на нулевое место
    list.pop(len(list) - 1)               # удаляем последний элемент
    i += 1
print(list)
"""

# Метод №2 через for

list = [1, 2, 3, 4, 5]

number = int(input('Введите число, на которое сдвинем массив: '))
i = 0
for _ in range(number):
    list.insert(0, list[len(list) - 1])   # последний индекс вставляем на нулевое место
    list.pop(len(list) - 1)               # удаляем последний элемент
print(list)


