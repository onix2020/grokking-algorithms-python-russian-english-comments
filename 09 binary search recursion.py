# Создаем функцию, которая принимает 4 входных параметра:
# список, его нижняя и верхняя границы, значение для поиска.
# Эта функция возращает индекс элемента, который находится в поиске.


def binary_search(list, low, high, item):
    # Проверяем правильность заданных границ списка.
    if high >= low:
        # Высчитываем индекс элемента в середине списка, округляя его в меньшую сторону.
        mid = low + (high - low) // 2

        # Определяем базовый случай функции
        # как если бы список содержал всего один элемент (и этот элемент был бы в середине массива соотвественно),
        # то этот элемент являлся бы наибольшим.
        # Если нужный элемент совпадает с тем, что находится в середине,
        # то возвращаем индекс этого элемента в середине массива.
        if list[mid] == item:
            return print("Искомый элемент находится под индексом %d" % mid)

        # Иначе если нужный элемент меньше того, что находится в середине списка,
        # тогда вызываем рекурсивно функцию, как если бы мы искали только в левой части списка,
        # то есть от начала до элемента в середине, не включая его.
        # При этом мы не используем срезы, а только изменяем переменные,
        # обозначающие верхнюю и нижнюю границы списка для поиска.
        elif list[mid] > item:
            return binary_search(list, low, mid - 1, item)

        # Если же нужный элемент больше того, что находится в середине списка,
        # тогда вызываем рекурсивно функцию, как если бы мы искали только в правой части массива,
        # то есть до конца списка от элемента в середине, не включая его.
        # При этом мы снова не используем срезы, а только изменяем переменные,
        # обозначающие верхнюю и нижнюю границы списка для поиска.
        else:
            return binary_search(list, mid + 1, high, item)

    # Иначе если заданы неверно границы списка
    # или не сработало ни одного из трех условий для поиска (то есть необходимое значение отсутствует в списке),
    # то выводим соответствующее сообщение об ошибке.
    else:
        return print("Искомого элемента нет списке или неверно указаны границы списка")


list1 = [2, 3, 4, 10, 40]
x = 3
y = 7

binary_search(list1, 0, len(list1) - 1, x) # все задано правильно
binary_search(list1, 10, len(list1) - 1, x) # неверно указана нижняя граница списка
binary_search(list1, 0, len(list1) - 1, y) # указано отсутствующее значение в списке для поиска