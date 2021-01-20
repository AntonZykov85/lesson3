def my_func():
    user_param_str = (input('введите три числа a, b , c '))
    user_param_list = user_param_str.split()
    ''' если бы было больше трех позиций наверно нужно применять функцю .sorted, также можно прогнать через if a>b elif ... else, но так получается много кода и я попробовал схитрить =) '''
    sum = int(user_param_list[0]) + int(user_param_list[1]) + int(user_param_list[2]) - int(min(user_param_list))
    return sum
print(my_func())

''' решение с вводом чисел в print'e '''
def my_func(a, b, c):
    sum = a + b + c - min(a, b, c)
    return sum
print(my_func(20, 45, 88))
