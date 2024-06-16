import re

text = """
Spotkanie odbędzie się w Poniedziałek, 10 stycznia 2023 roku. Na spotkaniu będzie 100 osób, a 50 z nich to studenci. Prowadzący: Dr. Nowak.
Proszę przynieść dokumenty nr 12345 oraz 67890. Sala wykładowa: B12. Adres: Ul. Wielka 5/6, 00-950 Warszawa. Telefon: +48 123 456 789.
Zamówienie nr 45678 zostało zrealizowane. Nowy termin: 02/03/2023. Koszt: 250 zł. Numer karty: 1234-5678-9876-5432.
Proszę zapisać się na newsletter na stronie www.przyklad.pl. Kolejne spotkanie odbędzie się 15 kwietnia 2023 roku.
"""

# Wyrażenie regularne do dopasowania słów zaczynających się od wielkiej litery
capitalized_words_pattern = r""

# Wyrażenie regularne do dopasowania liczb całkowitych
integer_pattern = r""

# Wyrażenie regularne do dopasowania słów kończących się znakiem interpunkcyjnym
punctuated_words_pattern = r""

# Znalezienie wszystkich dopasowań
capitalized_words = re.findall(capitalized_words_pattern, text)
integers = re.findall(integer_pattern, text)
punctuated_words = re.findall(punctuated_words_pattern, text)

# Wyświetlenie wyników
print("Znalezione słowa zaczynające się od wielkiej litery:", capitalized_words)
print("Znalezione liczby całkowite:", integers)
print("Znalezione słowa kończące się znakiem interpunkcyjnym:", punctuated_words)
