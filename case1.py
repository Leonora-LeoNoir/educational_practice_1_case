from datetime import date
import calendar

#Словарь матрица трафарета каждой буквы
digits = {
    '0': ["*** ", "* * ", "* * ", "* * ", "*** "],
    '1': ["  * ", "  * ", "  * ", "  * ", "  * "],
    '2': ["*** ", "  * ", "*** ", "*   ", "*** "],
    '3': ["*** ", "  * ", "*** ", "  * ", "*** "],
    '4': ["* * ", "* * ", "*** ", "  * ", "  * "],
    '5': ["*** ", "*   ", "*** ", "  * ", "*** "],
    '6': ["*** ", "*   ", "*** ", "* * ", "*** "],
    '7': ["*** ", "  * ", "  * ", "  * ", "  * "],
    '8': ["*** ", "* * ", "*** ", "* * ", "*** "],
    '9': ["*** ", "* * ", "*** ", "  * ", "*** "]
}

#функция для определения дня недели
def get_day_of_week(birth_date):
    days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
    return days[birth_date.weekday()]

#функция для определения возраста
def calculate_age(birth_date):
    today = date.today()
    # Логическое выражение вернет True (1) или False (0), заменяя блок if
    return today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

#функция для реализации шрифта *звездочка
def print_date_block(birth_date):
    full_date = f"{day:02d}{month:02d}{year:04d}"

    for i in range(5):
        line = ""
        for char in full_date:
            line += digits[char][i] + "  " 
        print(line)

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

print(print_date_block(user_date))


