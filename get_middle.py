# Вам будет предоставлена непустая строка. Ваша задача — вернуть средний
# (средние) символы этой строки.

# Если длина строки нечетная, верните средний символ.
# Если длина строки четная, верните два средних символа.
# Примеры:
# "test" --> "es"
# "testing" --> "t"
# "middle" --> "dd"
# "A" --> "A"

def get_middle(s):
    if len(s) % 2 != 0:
        return s[len(s) // 2]
    else:
        return s[len(s) // 2 - 1:len(s) // 2 + 1]

#def get_middle(s):
#    mid = len(s) // 2
#    return s[mid] if len(s) % 2 else s[mid-1:mid+1]

print(get_middle('middle'))
