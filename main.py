from zarzadzanie_danymi import zapisz_saldo, odczytaj_saldo, zapisz_operacje, odczytaj_historie_operacji, \
    zapisz_magazyn, zapisz_saldo_do_pliku


def komendy():
    print("Witam w twoim magazynie, dostępne komendy to:")
    print("Saldo - Wyświetl saldo konta firmy")
    print("Sprzedaż - Zarejestruj sprzedaż")
    print("Zakup - Zarejestruj zakup")
    print("Konto - Wyświetl szczegóły konta firmy")
    print("Lista - Wyświetl listę wszystkich operacji")
    print("Stan_magazynu - Wyświetl stan magazynu")
    print("Przegląd - Wyświetl przegląd operacji i stanu magazynu")
    print("Koniec - Zakończ program")
    if saldo_dodaj_odejmij:
        print("Dodaj saldo - Dodaj kwotę do salda konta")
        print("Odejmij saldo - Odejmij kwotę od salda konta")


def modyfikuj_saldo(operacja, saldo):
    kwota = float(input(f"Podaj kwotę do {operacja} (PLN): "))
    if operacja == "dodaj saldo":
        saldo += kwota
    elif operacja == "odejmij saldo":
        if kwota <= saldo:
            saldo -= kwota
        else:
            print("Brak wystarczających środków na koncie.")
    else:
        print("Niepoprawna operacja. Użyj 'dodaj saldo' lub 'odejmij saldo.'")
    zapisz_saldo_do_pliku(saldo)
    print(f"{operacja.capitalize()} {kwota} PLN do salda konta. Aktualne saldo: {saldo} PLN")
    return saldo



def zarejestruj_sprzedaz(saldo, historia_operacji):
    produkt = input("Podaj nazwę sprzedawanego produktu: ")
    cena = float(input("Podaj cenę produktu (PLN): "))
    ilosc = int(input("Podaj ilość sprzedanych produktów: "))
    kwota_sprzedazy = cena * ilosc
    saldo += kwota_sprzedazy
    operacja = f"Sprzedaż: {ilosc} sztuk {produkt} za {kwota_sprzedazy} PLN"
    historia_operacji.append(operacja)
    zapisz_operacje(operacja)

    with open("saldo_magazyn.txt", "w") as file:
        file.write(f"Saldo twojego konta wynosi: {saldo} PLN\n")

    print(f"Zarejestrowano sprzedaż {ilosc} sztuk {produkt} za {kwota_sprzedazy} PLN")
    return saldo, historia_operacji




def zarejestruj_zakup(saldo, magazyn, historia_operacji):
    produkt = input("Podaj nazwę zakupionego produktu: ")
    cena = float(input("Podaj cenę produktu (PLN): "))
    ilosc = int(input("Podaj ilość zakupionych produktów: "))
    kwota_zakupu = cena * ilosc
    saldo -= kwota_zakupu
    if produkt in magazyn:
        magazyn[produkt]["stan magazynu(sztuk)"] += ilosc
    else:
        print("Produkt nie istnieje w magazynie. Dodano nowy produkt.")
        magazyn[produkt] = {"stan magazynu(sztuk)": ilosc, "cena": cena}
    operacja = f"Zakup: {ilosc} sztuk {produkt} za {kwota_zakupu} PLN"
    historia_operacji.append(operacja)
    zapisz_magazyn(magazyn)
    print(f"Zarejestrowano zakup {ilosc} sztuk {produkt} za {kwota_zakupu} PLN")
    return saldo, magazyn, historia_operacji


def wyswietl_konto(saldo, magazyn):
    print(f"Saldo konta firmy: {saldo} PLN")
    print("Szczegóły konta firmy:")
    for produkt, dane in magazyn.items():
        print(f"{produkt}: Stan magazynu: {dane['stan magazynu(sztuk)']} sztuk, Cena: {dane['cena']} PLN/sztuka")


def historia_operacji_wyswietl(historia_operacji):
    print("Historia operacji:")
    for operacja in historia_operacji:
        print(operacja)


def wyswietl_magazyn(magazyn):
    print("Stan magazynu:")
    for produkt, dane in magazyn.items():
        print(f"{produkt}: Stan magazynu: {dane['stan magazynu(sztuk)']} sztuk, Cena: {dane['cena']} PLN/sztuka")


def przeglad(saldo, magazyn, historia_operacji):
    historia_operacji_wyswietl(historia_operacji)
    wyswietl_konto(saldo, magazyn)
    wyswietl_magazyn(magazyn)



saldo = 10000
zapisz_saldo(saldo)
saldo = odczytaj_saldo()
magazyn = {
    "Łódka": {"stan magazynu(sztuk)": 4, "cena": 1500},
    "Wędka": {"stan magazynu(sztuk)": 8, "cena": 400},
    "Przynęta": {"stan magazynu(sztuk)": 200, "cena": 15}
}
zapisz_saldo(saldo)
historia_operacji = odczytaj_historie_operacji()
zapisz_saldo_do_pliku(saldo)



saldo_dodaj_odejmij = False

while True:
    komendy()
    komenda = input("Podaj komendę: ").strip().lower()

    if komenda == "saldo":
        if not saldo_dodaj_odejmij:
            print("Saldo konta firmy:", saldo)
            saldo_dodaj_odejmij = True
    elif komenda == "dodaj saldo" and saldo_dodaj_odejmij:
        saldo += float(input("Podaj kwotę do dodania (PLN): "))
        print("Saldo zostało zaktualizowane i wynosi", saldo)
    elif komenda == "odejmij saldo" and saldo_dodaj_odejmij:
        kwota = float(input("Podaj kwotę do odjęcia (PLN): "))
        if kwota <= saldo:
            saldo -= kwota
            print("Saldo zostało zaktualizowane i wynosi", saldo)
        else:
            print("Brak wystarczających środków na koncie.")
    elif komenda == "sprzedaż":
            saldo, historia_operacji = zarejestruj_sprzedaz(saldo, historia_operacji)
    elif komenda == "zakup":
        saldo, magazyn, historia_operacji = zarejestruj_zakup(saldo, magazyn, historia_operacji)
    elif komenda == "konto":
        wyswietl_konto(saldo, magazyn)
    elif komenda == "lista":
        historia_operacji_wyswietl(historia_operacji)
    elif komenda == "stan_magazynu":
        wyswietl_magazyn(magazyn)
    elif komenda == "przegląd":
        przeglad(saldo, magazyn, historia_operacji)
    elif komenda == "koniec":
        break
    else:
        print("Niepoprawna komenda. Spróbuj ponownie.")



