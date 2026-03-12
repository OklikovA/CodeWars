# Дана последовательность цифр. Необходимо заменить все цифры меньше 5 на
# '0', а все цифры от 5 до 1 на '1'. Верните полученную строку.
# Примечание: введенная строка никогда не будет пустой.

def fake_bin(x):
    result = []
    for digit in x:
        if int(digit) < 5:
            result.append('0')
        else:
            result.append('1')
    return ''.join(result)


x = "45385593107843568"
print(fake_bin(x))
