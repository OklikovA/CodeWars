# На вход программе подается строка с номером телефона. Ожидается следующий
# формат номера в строке:
# +7(xxx)xxx-xx-xx
# где x - это любая цифра. Число введенных символов считается верным (то
# есть, не может быть,
# чтобы отсутствовала какая-либо цифра или была лишняя). Необходимо
# прочитать строку из входного потока и проверить,
# что она содержит номер телефона в соответствии с приведенным форматом.
# Вывести "ДА", если это так и "НЕТ" в противном случае.

phone = input()
valid_phone = True

if len(phone) != 16:
    valid_phone = False

else:
    for i, char in enumerate(phone):
        if i == 0 and char != '+':
            valid_phone = False
            break
        elif i == 1 and char != '7':
            valid_phone = False
            break
        elif i == 2 and char != '(':
            valid_phone = False
            break
        elif i == 6 and char != ')':
            valid_phone = False
            break
        elif i == 10 and char != '-':
            valid_phone = False
            break
        elif i == 13 and char != '-':
            valid_phone = False
            break
        elif i in (3, 4, 5, 7, 8, 9, 11, 12, 14, 15):
            if not char.isdigit():
                valid_phone = False
                break

print('ДА' if valid_phone else 'НЕТ')
