def my_sum():
 s = 0
 try:
    while True:
             for user_numb in map(int, input('введите числа через пробел. Для закрытия программы нажмите любую букву ').split()):
                 s += user_numb
             print(s)
 except ValueError:
             print(s)

 #return(my_sum()) - почему не нужен ретурн? потому что принты два раза?
print(my_sum())

''' https://ru.stackoverflow.com/questions/459401 - перевод строки в число загуглил тут'''
