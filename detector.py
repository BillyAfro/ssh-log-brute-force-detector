"""
SSH Log Brute Force Detector
Status: In Development (W trakcie rozwoju do przetestowania 22.04.2026)
Autor: BillyAfro 
Wersja: 1.0 Beta
"""

import re  # Biblioteka do wyszukiwania wzorców w tekście
from collections import defaultdict # Umożliwia tworzenie słowników, które automatycznie inicjują nowe klucze

LOG_FILE = "data/auth.log"  # Musimy zdefiniować, jaki plik otwieramy
failed_logins = defaultdict(int)  # Tworzy słownik do przechowywania adresów IP i liczby ich błędnych logowań
pattern = re.compile(r"Failed password.*from (\d+\.\d+\.\d+\.\d+)")  # Definiuje wzorzec, który wyszukuje nieudane logowania

# KROK 1: Czytamy plik i zliczamy wszystko do "zeszytu" (słownika)
with open(LOG_FILE, "r") as file: # Otwiera plik logów w trybie odczytu
    for line in file:  # Pętla, która bierze do ręki każdą kolejną linijkę z pliku
        match = pattern.search(line)  # Próbuje dopasować wzorzec do aktualnej linii
        if match:  # Jeśli wzorzec został znaleziony...
            ip_address = match.group(1)  # Wyciąga sam adres IP
            failed_logins[ip_address] += 1  # Zwiększa licznik prób dla tego IP o 1

# KROK 2: Kiedy plik jest już zamknięty, przeglądamy wyniki i filtrujemy agresorów
for ip, count in failed_logins.items(): # Przegląda Twój "zeszyt" z wynikami
    if count > 5:  # Dopiero TUTAJ sprawdzamy, czy prób było więcej niż 5
        print(f"IP: {ip} - Proby: {count}")  # Wypisuje tylko tych, którzy przesadzili z próbami 
