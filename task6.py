def int_func():
    word_str = input('введите слово ')
    return word_str.title()
print(int_func())

def int_func():
   i = 0
   word_list = input('введите слова через пробел ').split()
   print(word_list)
   while i <= len(word_list) - 1:
        word_list[i] = word_list[i].title()
        i += 1
   return word_list
print(int_func())

"""если честно я не понял, что нужно сделать в задании (читали с женой вдвоем), режил что в задании 7 необходимо создать список и начать его с большой буквы"""