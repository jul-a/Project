import re

with open('data.txt', 'r') as file:
    text = file.read()

pattern = r""  # Uzupełnij wyrażenie regularne
phone_numbers = re.findall(pattern, text)
print("Znalezione numery telefonow:", phone_numbers)

