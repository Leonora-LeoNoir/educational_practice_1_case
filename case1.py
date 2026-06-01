from datetime import datetime
import calendar

def get_day_of_week(year, month, day): # Создаем объект даты
    date_obj = datetime(year, month, day)
    
    # weekday() возвращает число от 0 (понедельник) до 6 (воскресенье)
    days = [
        "Понедельник", "Вторник", "Среда", 
        "Четверг", "Пятница", "Суббота", "Воскресенье"
    ]
    
    return days[date_obj.weekday()]

print('Число вашего рождения (цифрами):') #текст подсказка для пользователя
day = int(input()) #строка ввода
print('Месяц вашего рождения (цифрами):') #текст подсказка для пользователя
month = int(input()) #строка ввода
print('Год вашего рождения (цифрами):') #текст подсказка для пользователя
year = int(input()) #строка ввода

print(get_day_of_week(year, month, day))

if calendar.isleap(year):
    print('Год високосный.')
else:
    print('Год не високосный.')

