def my_func():
    try:
      a = int(input('введите число'))
      b = int(input('введите число'))
      c = a / b
    except ZeroDivisionError:
        return "На ноль делить нельзя!"
    return c
print(my_func())

'''правильно я понял, что except работает только если есть трай?'''