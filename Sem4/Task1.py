# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию .split()

string = 'd g h t r g r h t j h b v f d s d f'
print(string)

my_list = string.split()
my_dict = {}
new_list = []

for letter in my_list:
    my_dict[letter] = my_dict.get(letter, 0) + 1
    if my_dict.get(letter) > 1:
        new_list.append(letter + '_' + str(my_dict.get(letter)))
    else:
        new_list.append(letter)

print(' '.join(new_list))
