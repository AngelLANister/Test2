def season_of_year(month):
    if 3 <= month <= 5:
        return "Весна"
    if 6 <= month <= 8:
        return "Лето"
    if 9 <= month <= 11:
        return "Осень"
    if 1 <= month <= 2 or month == 12:
        return "Зима"
    return "Неверный номер месяца"


month = int(input("Введите номер месяца (1-12): "))
print(season_of_year(month))
