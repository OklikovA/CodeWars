# Создайте функцию, которая принимает целое число в качестве аргумента и
# возвращает значение "Even"для четных чисел или "Odd"для нечетных чисел.

def even_or_odd(number):
    """
    Выводит Even если число четное, Odd если не четное
    :param number:
    :return:
    """
    return 'Even' if number % 2 == 0 else 'Odd'


number = int(input())
print(even_or_odd(number))
