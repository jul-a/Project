import re

text = """
Kontakt: email@example.com, data spotkania: 25/12/2022, strona internetowa: https://www.example.com.
Dodatkowy kontakt: info@test.com, data wydarzenia: 01/01/2023, odwiedź: http://test.com.
Skontaktuj się z nami na support@domain.org, wydarzenie odbędzie się 15/08/2022, więcej informacji na stronie: https://info.example.org.
Zapraszamy do rejestracji na webinarze: webinar@events.com, termin: 20/11/2021, link: http://webinar.com/signup.
Jeśli masz pytania, napisz na: questions@faq.com, data zakończenia: 30/09/2022, szczegóły na: https://faq.com/details.
"""

# Wyrażenie regularne do dopasowania adresów e-mail
# Jeden lub więcej znaków alfanumerycznych, kropek lub myślników przed znakiem @.
# Znak @.
# Jeden lub więcej znaków alfanumerycznych, kropek lub myślników po znaku @.
# Jedna kropka.
# Domena o długości od 2 do 6 znaków alfabetycznych.
email_pattern = r""

# Wyrażenie regularne do dopasowania dat w formacie DD/MM/YYYY
date_pattern = r""

# Wyrażenie regularne do dopasowania adresów URL
# Prefiks http:// lub https://.
# Jeden lub więcej znaków alfanumerycznych, kropek lub myślników dla domeny.
# Jedna kropka.
# Domena o długości od 2 do 6 znaków alfabetycznych.
url_pattern = r""

# Znalezienie wszystkich dopasowań
emails = re.findall(email_pattern, text)
dates = re.findall(date_pattern, text)
urls = re.findall(url_pattern, text)

print("Znalezione adresy e-mail:", emails)
print("Znalezione daty:", dates)
print("Znalezione adresy URL:", urls)
