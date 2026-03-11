#Создайте функцию, которая принимает целое число в качестве аргумента и
# возвращает значение "Even"для четных чисел или "Odd"для нечетных чисел.

def even_or_odd(number):
    if number % 2 == 0:
        return 'Even'
    else:
        return 'Odd'


number = int(input())
res = even_or_odd(number)
print(res)