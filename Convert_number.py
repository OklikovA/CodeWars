# Дано случайное неотрицательное число, и необходимо вернуть цифры этого
# числа в массиве в обратном порядке.

def digitize(n):
    """
    Выводит число в обратном порядке
    :param n:
    :return:
    """
    return [int(digit) for digit in str(n)[::-1]]


n = int(input())
result = digitize(n)
print(result)
