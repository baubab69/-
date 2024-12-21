def add(a, b):
    return a +b
a = input('Your name:')
b = '- sexy'
print(a, b)
def zodiac(year):
    animals = ["Крыса", "Бык", "Тигр", "Кролик", "Дракон", "Змея", "Лощадь", "Коза", "Обезьяна", "Петух", "Собака", "Свинья"]
    start_year = 1900
    index = (year - start_year)%12
    return animals[index]
def is_leap(year):
    leap = 'Not cool'

    if year %400 == 0:
        leap = 'Cool!'
    elif year %100 != 0:
        leap = 'Not cool'
    elif year %4 == 0:
        leap = 'Cool!'
    else:
        leap = 'Not cool'
    return leap
def mean(year):
      zodiac_sign = zodiac(year)
      is_leap_sign = is_leap(year)
      return f"{zodiac_sign}\n{is_leap_sign}"
year = int(input('Year of birth:'))
print(mean(year))

    