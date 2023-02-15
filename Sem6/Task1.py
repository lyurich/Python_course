# Дан список чисел. Посчитайте сколько в ней пар элементов, равных друг другу.
# Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.


from random import randint

size = int(input('Введите размер списка: '))
user_list = []
for _ in range(size):
    user_list.append(randint(0, 5))
print(user_list)
user_list.sort()
print(user_list)

user_set = set(user_list)

count_double = 0
list_undouble = []
for item_set in user_set:
    count_double += user_list.count(item_set) // 2
    if user_list.count(item_set) % 2 != 0:
        list_undouble.append(item_set)
print(f'Число пар в списке: {count_double}')
print(f'Числа без пар: {list_undouble}')