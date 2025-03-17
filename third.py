import re

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

def formatted_numbers(phone_number):
    # Видаляємо всі зайві символи
    clean_number = re.sub(r"[^\d+]", "", phone_number)

    # додаємо "+38"
    if not re.match(r"^\+?380", clean_number):
        clean_number = "+38" + clean_number.lstrip("0")  # Прибираємо зайві "0" на початку

    return clean_number

sanitized_numbers = [formatted_numbers(num) for num in raw_numbers]

print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)