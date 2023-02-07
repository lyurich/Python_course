# Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea shore shells
# Output: 13

string = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure. So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"
my_list = string.split()
print(my_list)
new_list = set(my_list)
print(new_list)
print(len(new_list))