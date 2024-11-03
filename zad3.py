import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-m',
                        '--miesiece',
                        nargs='+',
                        choices=["styczeń", "luty", "marzec", "kwiecień", "maj", "czerwiec", "lipiec",
                                 "sierpień", "wrzesień", "październik", "listopad", "grudzień"],
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

    #TODO
    #wykonaj(args.miesiace, args.dni, args.pory, tryb)


if __name__ == '__main__':
    main()