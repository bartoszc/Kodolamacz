class Zwierze:
    def __init__(self, nazwa, wiek, waga):
        self.nazwa = nazwa
        self.wiek = wiek
        self.waga = waga

    def przedstaw_sie(self):
        print(f"Jestem zwierzęciem {self.nazwa}, mam {self.wiek} lat oraz wazę {self.waga} kg.")

    def urodziny(self):
        self.wiek += 1


class Slon(Zwierze):
    def przedstaw_sie(self):
        print(f"Jestem słoniem {self.nazwa}, mam {self.wiek} lat oraz wazę {self.waga} kg.")


class Lew(Zwierze):
    def przedstaw_sie(self):
        super().przedstaw_sie()
        print("A tak w ogóle to jestem lwem")


class Papuga(Zwierze):
    def __init__(self, nazwa, wiek, waga, kolor):
        super().__init__(nazwa, wiek, waga)
        self.kolor = kolor

    def przedstaw_sie(self):
        super().przedstaw_sie()
        print(f"Jako papuga mój kolor to {self.kolor}")


def nowy_rok(zoo):
    for zwierze in zoo:
        zwierze.urodziny()


def przedstaw_zwierzeta(zoo):
    for zwierze in zoo:
        zwierze.przedstaw_sie()


def main():
    Dumboo = Slon("Dumboo", 77, 6000)
    Simba = Lew("Simba", 24, 100)
    # Jago = Papuga("Jago", 32, 3) # będzie błąd
    Jago = Papuga("Jago", 32, 3, "czerwony")
    jakis_zwierz = Zwierze("Katarzyna", 31, 80)

    Dumboo.przedstaw_sie()
    Simba.przedstaw_sie()
    jakis_zwierz.przedstaw_sie()

    Jago.urodziny()
    Jago.przedstaw_sie()

    print(f"isinstance(Dumboo, Slon): {isinstance(Dumboo, Slon)}")
    print(f"isinstance(Dumboo, Lew): {isinstance(Dumboo, Lew)}")
    print(f"isinstance(Jago, Papuga): {isinstance(Jago, Papuga)}")
    print(f"isinstance(Jago, Zwierze): {isinstance(Jago, Zwierze)}")
    print(f"isinstance(jakis_zwierz, Zwierze): {isinstance(jakis_zwierz, Zwierze)}")
    print(f"isinstance(jakis_zwierz, Papuga): {isinstance(jakis_zwierz, Papuga)}")

    zoo = [Dumboo, Simba, Jago, jakis_zwierz]
    nowy_rok(zoo)
    przedstaw_zwierzeta(zoo)


if __name__ == "__main__":
    main()
