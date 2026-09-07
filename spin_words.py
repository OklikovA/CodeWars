# Напишите функцию, которая принимает на вход строку из одного или
# нескольких слов и возвращает ту же строку, но со всеми словами, в которых
# пять или более букв перевернуты (как в названии этого задания).
# Передаваемые строки будут состоять только из букв и пробелов. Пробелы
# будут добавляться только в том случае, если присутствует более одного слова.

# Примеры:
# "Hey fellow warriors"  --> "Hey wollef sroirraw"
# "This is a test        --> "This is a test"
# "This is another test" --> "This is rehtona test"

def spin_words(sentence):
    #Проверка длины слова
    for word in sentence:
        if len(word) >= 5:
            #Если слово длиннее 5 символов переворачиваем
            lst.append(word[::-1])
        else:
            lst.append(word)
    return lst


sentence = list(input().split())
lst = []
print(*spin_words(sentence))
