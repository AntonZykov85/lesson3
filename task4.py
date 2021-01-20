def my_func(x, y):
    if x <= 0:
        print('значение "х" не является положительным')
    elif y >= 0:
        print('значение "y" не является отрицательным')
    else:
        exp = x ** y
        return exp

print(my_func(5, -2))

def my_func1(x, y):
    if x <= 0:
        print('значение "х" не является положительным')
    elif y >= 0:
        print('значение "y" не является отрицательным')
    else:
        y = abs(y)
        i = 0
        while i < y:
            x *= x
            i += 1
            exp = 1 / x
            return exp
print(my_func(-1, 0))
