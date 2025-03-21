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

def normalize_phone(phone_number):
    # залишити тільки цифри та "+"
    clean_number = re.sub(r"[^\d+]", "", phone_number).strip()
    
    # вже починається на +380, нічого не змінюємо
    if re.match(r"^\+380", clean_number):
        return clean_number
    
    # починається з 380 без "+", додаємо +
    if re.match(r"^380", clean_number):
        return "+" + clean_number
    
    # починається з 0, замінюємо на +380
    if clean_number.startswith("0"):
        return "+380" + clean_number.lstrip("0")

    #все ок
    return clean_number

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]


print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)