from datetime import datetime

def get_days_from_today(date_string):
    try:
        # Перетворюємо рядок у дату
        given_date = datetime.strptime(date_string, "%Y-%m-%d").date()
        # Отримуємо поточну дату без часу
        current_date = datetime.today().date()
        # Обчислюємо різницю в днях
        days_difference = (current_date - given_date).days
        return days_difference
    except ValueError:
        return "Невірний формат дати! Використовуйте 'РРРР-ММ-ДД'"

# Приклади роботи:
print(get_days_from_today("2021-10-09"))  
print(get_days_from_today("2030-01-01"))  
print(get_days_from_today("10-09-2021"))  