# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

from random import randint
my_list = []
for _ in range(15):
    my_list.append(randint(0, 9)) # append - добавляет элементы в существующий список

print(my_list)

print(set(my_list))  # set выводит все уникальные элементы, т.е. отбрасывает повторяющиеся
print(len(set(my_list)))