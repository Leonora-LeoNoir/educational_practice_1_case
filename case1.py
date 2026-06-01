from datetime import date
import calendar

#функция для определения дня недели
def get_day_of_week(birth_date):
    days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
    return days[birth_date.weekday()]

#функция для определения возраста
def calculate_age(birth_date):
    today = date.today()
    # Логическое выражение вернет True (1) или False (0), заменяя блок if
    return today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

print('Число вашего рождения (цифрами):') #текст подсказка для пользователя
day = int(input()) #строка ввода
print('Месяц вашего рождения (цифрами):') #текст подсказка для пользователя
month = int(input()) #строка ввода
print('Год вашего рождения (цифрами):') #текст подсказка для пользователя
year = int(input()) #строка ввода

user_date = date(year, month, day)

print(get_day_of_week(user_date))

if calendar.isleap(year):
    print('Год високосный.')
else:
    print('Год не високосный.')

print(f"Вам сейчас: {calculate_age(user_date)} лет")

