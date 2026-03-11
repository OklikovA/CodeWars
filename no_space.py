# Напишите функцию, которая удаляет пробелы из строки, а затем возвращает
# результирующую строку.

def no_space(x):
    """
    Удаляет пробелы
    :param x:
    :return: Текст без пробелов
    """
    str = x.replace(" ", "")
    return(str)

x = input()
nospase = no_space(x)
print(nospase)

