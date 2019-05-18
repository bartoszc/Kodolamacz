from abc import ABC, abstractmethod


class Zwierze(ABC):
    def __init__(self, nazwa, wiek, waga):
        self.nazwa = nazwa
        self.wiek = wiek
        self.waga = waga

    @abstractmethod  # tutaj wymuszamy implementację tej metody w klasach pochodnych
    def nazwa_gatunku(self):
        pass

    def przedstaw_sie(self):
        print(f"Jestem {self.nazwa_gatunku()}. Mam na imię {self.nazwa}, mam {self.wiek} lat oraz wazę {self.waga} kg.")

    def urodziny(self):
        self.wiek += 1


class Slon(Zwierze):
    def nazwa_gatunku(self):
        return "Słoń"


class Lew(Zwierze):
    def nazwa_gatunku(self):
        return "Lew"


class Papuga(Zwierze):
    def nazwa_gatunku(self):
        return "Papuga"

    def __init__(self, nazwa, wiek, waga, kolor):
        super().__init__(nazwa, wiek, waga)
        self.kolor = kolor

    def przedstaw_sie(self):
        super().przedstaw_sie()
        print(f"Jako papuga mój kolor to {self.kolor}")


def main():
    Dumboo = Slon("Dumboo", 77, 6000)
    Simba = Lew("Simba", 24, 100)
    Jago = Papuga("Jago", 32, 3, "czerwony")
    # jakis_zwierz = Zwierze("Katarzyna", 31, 80) # będzie błąd

    Dumboo.przedstaw_sie()
    Simba.przedstaw_sie()
    # jakis_zwierz.przedstaw_sie()

    Jago.urodziny()
    Jago.przedstaw_sie()


if __name__ == "__main__":
    main()
