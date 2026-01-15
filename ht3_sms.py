import re

def normalize_phone(phone_number: str) -> str:
    s = phone_number.strip()

    s = re.sub(r"^\s*00", "+", s)

    digits = re.sub(r"\D", "", s)

    if s.lstrip().startswith("+"):
        normalized = "+" + digits
    else:
        if digits.startswith("380"):
            normalized = "+" + digits
        else:
            normalized = "+38" + digits

    normalized = "+" + re.sub(r"\D", "", normalized)

    if re.fullmatch(r"\+380\d{9}", normalized):
        return normalized
    return ""

raw_numbers = [
    "067\t123 4567",
    "(095) 234-5678\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38063-161-22-22",
    "38050 111 22 11   ",                                                      
    "тел: 050-123-45-67",        
    "++380971234567",            
    "+38+0501234567",            
    "+(380)50(957)45-67",        
    "00380537634567",            
    "380 60 123 45 67 ext 99",   
    "0501365567#",              
    "050-12-34",                 
    "38050123",                                            
    "090/123\\45|67",            
    " ( 0 5 0512346 7 ", 
    "+38 (050) 123-32-34 !!!",   
    "0503451234  ",             
    "\t+380(97)123-45-67\t", 
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
sanitized_numbers = [n for n in sanitized_numbers if n]

print("Нормалізовані номери телефонів для SMS-розсилки:")
for number in sanitized_numbers:
    print(number)