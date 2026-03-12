def quarter_of(month):
    if month < 1  or month > 12:
        return 'ERROR'
    elif 1 <= month <= 3:
        return 1
    elif 4 <= month <= 6:
        return 2
    elif 7 <= month <= 9:
        return 3
    elif 10 <= month <= 12:
        return 4


month = int(input())
print(quarter_of(month))
