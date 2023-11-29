import os


def zapisz_saldo(saldo):
    with open("saldo_magazyn.txt", "w") as saldo_file:
        saldo_file.write(str(saldo))

def zapisz_saldo_do_pliku(saldo):
    try:
        with open("saldo_magazyn.txt", "w") as file:
            file.write(f"Saldo twojego konta wynosi: {saldo} PLN\n")
        print("Saldo zostało zapisane do pliku saldo_magazyn.txt.")
    except Exception as e:
        print(f"Wystąpił błąd podczas zapisywania salda: {str(e)}")

def zapisz_magazyn(magazyn):
    with open("magazyn.txt", "w") as file:
        for produkt, dane in magazyn.items():
            file.write(f"{produkt}: Stan magazynu: {dane['stan magazynu(sztuk)']} sztuk, Cena: {dane['cena']} PLN/sztuka\n")

def odczytaj_saldo():
    try:
        if os.path.exists("saldo_magazyn.txt"):
            with open("saldo_magazyn.txt", "r") as saldo_file:
                saldo = float(saldo_file.read())
            return saldo
        else:
            print("Plik saldo_magazyn.txt nie istnieje.")
            return None
    except Exception as e:
        print(f"Błąd odczytu salda: {e}")
        return None

def zapisz_operacje(operacja):
    try:
        with open("historia_operacji.txt", "a") as historia_file:
            historia_file.write(f"{operacja}\n")
    except Exception as e:
        print(f"Błąd podczas zapisu operacji: {e}")


def odczytaj_historie_operacji():
    try:
        if os.path.exists("historia_operacji.txt"):
            with open("historia_operacji.txt", "r") as historia_file:
                historia_operacji = [line.strip() for line in historia_file.readlines()]
            return historia_operacji
        else:
            print("Plik historia_operacji.txt nie istnieje.")
            return []
    except Exception as e:
        print(f"Błąd odczytu historii operacji: {e}")
        return []