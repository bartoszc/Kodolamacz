from abc import ABC, abstractmethod
import math


class Wezel(ABC):
    @abstractmethod
    def nazwa(self):
        pass

    def wypisz(self):
        print(f"Wykonuję {self.nazwa()}.", end=' ')

    @abstractmethod
    def wartosc(self):
        pass


class Liczba(Wezel):
    def __init__(self, liczba):
        self.liczba = liczba

    def nazwa(self):
        return "liczba"

    def wypisz(self):
        print(f"Jestem liczbą {self.liczba}")

    def wartosc(self):
        return self.liczba


class Suma(Wezel):
    def __init__(self, skladnik1, skladnik2):
        self.skladnik1 = skladnik1
        self.skladnik2 = skladnik2

    def nazwa(self):
        return "dodawanie"

    def wypisz(self):
        self.skladnik1.wypisz()
        self.skladnik2.wypisz()
        super().wypisz()
        print(f"{self.skladnik1.wartosc()}+{self.skladnik2.wartosc()}={self.wartosc()}")

    def wartosc(self):
        return self.skladnik1.wartosc() - self.skladnik2.wartosc()


class Roznica(Wezel):
    def __init__(self, odjemna, odjemnik):
        self.odjemna = odjemna
        self.odjemnik = odjemnik

    def nazwa(self):
        return "odejmowanie"

    def wypisz(self):
        self.odjemna.wypisz()
        self.odjemnik.wypisz()
        super().wypisz()
        print(f"{self.odjemna.wartosc()}-{self.odjemnik.wartosc()}={self.wartosc()}")

    def wartosc(self):
        return self.odjemna.wartosc() - self.odjemnik.wartosc()


class Iloczyn(Wezel):
    def __init__(self, czynnik1, czynnik2):
        self.czynnik1 = czynnik1
        self.czynnik2 = czynnik2

    def nazwa(self):
        return "mnożenie"

    def wypisz(self):
        self.czynnik1.wypisz()
        self.czynnik2.wypisz()
        super().wypisz()
        print(f"{self.czynnik1.wartosc()}*{self.czynnik2.wartosc()}={self.wartosc()}")

    def wartosc(self):
        return self.czynnik1.wartosc() * self.czynnik2.wartosc()


class Iloraz(Wezel):
    def __init__(self, dzielna, dzielnik):
        self.dzielna = dzielna
        self.dzielnik = dzielnik

    def nazwa(self):
        return "dzielenie"

    def wypisz(self):
        self.dzielna.wypisz()
        self.dzielnik.wypisz()
        super().wypisz()
        print(f"{self.dzielna.wartosc()}/{self.dzielnik.wartosc()}={self.wartosc()}")

    def wartosc(self):
        return self.dzielna.wartosc() / self.dzielnik.wartosc()


class Silnia(Wezel):
    def __init__(self, liczba):
        self.liczba = liczba

    def nazwa(self):
        return "silnia"

    def wypisz(self):
        self.liczba.wypisz()
        super().wypisz()
        print(f"{self.liczba.wartosc()}!={self.wartosc()}")

    def wartosc(self):
        return math.factorial(self.liczba.wartosc())


def main():
    minus_jeden = Liczba(-1)
    cztery = Liczba(4)
    piec = Liczba(5)
    siedem = Liczba(7)
    osiem = Liczba(8)

    dodawanie = Suma(piec, siedem)
    odejmowanie = Roznica(osiem, cztery)
    mnozenie = Iloczyn(dodawanie, odejmowanie)
    dzielenie = Iloraz(mnozenie, minus_jeden)
    silnia = Silnia(dzielenie)

    silnia.wypisz()


if __name__ == "__main__":
    main()
