import argparse
import csv
import os
import random


def wykonaj(miesiace, dni, pory, tryb):
    dni_tyg = ["pn", "wt", "sr", "cz", "pt", "sb", "nd"]
    if len(miesiace) != len(dni):
        print("Liczba dni tygodnia różna od liczby miesięcy")
        return

    wynik_odczytu = 0
    i = 0
    j = 0
    while i < len(miesiace):
        if '-' in dni[i]:
            flaga = False

            for dzien in dni_tyg:
                if dni[i][:2] == dzien:
                    flaga = True

                if flaga:
                    if j > len(pory) - 1:
                        pora = "r"
                    else:
                        pora = pory[j]

                    sciezka = os.path.join(miesiace[i], dzien, pora)
                    wynik_odczytu += wybor_akcji(tryb, sciezka)
                    j += 1

                if dni[i][3:5] == dzien:
                    flaga = False
        else:
            if j > len(pory) - 1:
                pora = "r"
            else:
                pora = pory[j]

            sciezka = os.path.join(miesiace[i], dni[i], pora)
            wynik_odczytu += wybor_akcji(tryb, sciezka)
            j += 1

        i += 1
    if not tryb:
        print(f"Wartosc odczytu: {wynik_odczytu}s")


def wybor_akcji(tryb, sciezka):
    if tryb:
        utworz_plik(sciezka)
        return 0
    else:
        return odczytaj_plik(sciezka)

def utworz_plik(sciezka):
    os.makedirs(sciezka, exist_ok=True)
    plik_csv = os.path.join(sciezka, "dane.csv")

    with open(plik_csv, mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Model', 'Wynik', 'Czas'])
        model = random.choice(['A', 'B', 'C'])
        wynik = random.randint(0, 1000)
        czas = f"{random.randint(0, 1000)}s"
        writer.writerow([model, wynik, czas])

    print(f"Utworzono plik: {plik_csv}")


def odczytaj_plik(sciezka):
    os.makedirs(sciezka, exist_ok=True)
    plik_csv = os.path.join(sciezka, "dane.csv")

    with open(plik_csv, newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')

        for row in reader:
            model = row['Model'].strip()
            czas = row['Czas'].strip()

            if model == 'A':
                return int(czas.replace('s', ''))

    return 0


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-m',
                        '--miesiace',
                        nargs='+',
                        choices=["styczen", "luty", "marzec", "kwiecien", "maj", "czerwiec", "lipiec",
                                 "sierpien", "wrzesien", "pazdziernik", "listopad", "grudzien"],
                        help="Wybierz miesiąc (dowolna liczba)"
                        )
    parser.add_argument('-d',
                        '--dni',
                        nargs='+',
                        choices=["pn", "wt", "sr", "cz", "pt", "sb", "nd",
                                 "pn-wt", "pn-sr", "pn-cz", "pn-pt", "pn-sb", "pn-nd",
                                 "wt-sr", "wt-cz", "wt-pt", "wt-sb", "wt-nd",
                                 "sr-cz", "sr-pt", "sr-sb", "sr-nd",
                                 "cz-pt", "cz-sb", "cz-nd", "pt-sb", "pt-nd", "sb-nd"],
                        help="Wybierz zakres dni (tyle samo co miesięcy)"
                        )
    parser.add_argument('-p',
                        '--pory',
                        nargs='+',
                        choices=["r", "w"],
                        default="r",
                        help="Wybierz porę dnia"
                        )
    parser.add_argument('-t',
                        '--tworz',
                        action='store_true',
                        help="Tworzy plik z podaną strukturą katalogów"
                        )
    parser.add_argument('-o',
                        '--odczyt',
                        action='store_true',
                        help="Czyta plik z podaną strukturą katalogów"
                        )
    args = parser.parse_args()

    if args.tworz:
        tryb = True
    if args.odczyt:
        tryb = False

    wykonaj(args.miesiace, args.dni, args.pory, tryb)


if __name__ == '__main__':
    main()