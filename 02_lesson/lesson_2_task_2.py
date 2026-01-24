def is_year_leap(year):
    return "Да" if year % 4 == 0 else "Нет"


year = int(input("Введите год: "))
result = is_year_leap(year)
print(f"{year} год - високосный? - {result}")
