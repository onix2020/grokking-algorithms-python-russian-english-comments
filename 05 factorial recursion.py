# Создаем рекурсивную функцию для вычисления факториала.
def fact(x):
    # Определяем базовый случай.
    # Если входной параметр будет равен 1, то функция вернет 1.
    if x == 1:
        return 1

    # Определяем рекурсивный случай.
    # Вызывается новая копия функции со входным параметром уменьшенным на 1.
    # Возвращаемое значение этой функции будет перемножено на входной параметр предыдущей вызванной функции.
    else:
        return x * fact(x-1)


print(fact(4))
