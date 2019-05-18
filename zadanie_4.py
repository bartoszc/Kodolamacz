class Osoba:
    def __init__(self, imie, nazwisko, wiek):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek

    def przedstaw_sie(self):
        print(f"Jestem {self.imie} {self.nazwisko}. Mam {self.wiek} lat.")

    def urodziny(self):
        wiek_przed = self.wiek
        self.wiek += 1
        return wiek_przed


class Test:
    def __init__(self):
        self.publiczne, self._chronione, self.__prywatne = 1, 2, 3


class Licznik:
    ile = 0                 # pole statyczne

    def __init__(self):     # konstruktor
        Licznik.ile += 1    # odwolanie do pola statycznego
        self.ktory = Licznik.ile
        print(f"To jest obiekt nr {Licznik.ile}")

    def __del__(self):      # destruktor, czyli kod, ktory wykonuje sie podczas niszczenia obiektu

        Licznik.ile -= 1
        print(f"Niszcze obiekt nr {self.ktory}, pozostalo jeszcze {Licznik.ile}.")

    @staticmethod
    def policz():
        return Licznik.ile


class FunkcjaKwadratowa:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def rozwiaz(self):
        if not self.a and not self.b and not self.c:
            print("To nie jest funkcja kwadratowa")
        else:
            delta = self.b ** 2 - (4 * self.a * self.c)
            if delta < 0:
                print("Funkcja nie ma miejsc zerowych")
            elif delta == 0:
                print(f"Funkcja ma jedno miejsce zerowe: {-self.b / (self.a * 2)}")
            else:
                import math
                x1 = (-self.b - math.sqrt(delta)) / (self.a * 2)
                x2 = (-self.b + math.sqrt(delta)) / (self.a * 2)
                print(f"Funkcja ma dwa miejsca zerowe: {x1} {x2}")


class Zespolona:
    def __init__(self, re, im):
        self.re = re
        self.im = im

    def modul(self):
        import math
        return math.sqrt(self.re ** 2 + self.im ** 2)

    @staticmethod
    def dodaj(l1, l2):
        return l1.re + l2.re + l1.im + l2.im

    @staticmethod
    def mnoz(l1, l2):
        return (l1.re * l2.re) - (l1.im * l2.im) + (l1.re * l2.im) + (l1.im * l2.re)


class Ulamek:
    def __init__(self, licznik, mianownik):
        if mianownik == 0:
            raise ZeroDivisionError("Mianownik równy zero.")
        self.licznik = licznik
        self.mianownik = mianownik

    def skroc(self):
        nwd = 1
        for i in range(1, self.mianownik+1):
            if self.licznik % i == 0 and self.mianownik % i == 0:
                nwd = i
        return self.licznik // nwd, self.mianownik // nwd

    @staticmethod
    def dodaj(u1, u2):
        return [(u1.licznik * u2.mianownik) + (u2.licznik * u1.mianownik), u1.mianownik * u2.mianownik]

    @staticmethod
    def odejmij(u1, u2):
        wynik = Ulamek((u1.licznik * u2.mianownik) - (u2.licznik * u1.mianownik), (u1.mianownik * u2.mianownik))
        return wynik.skroc()

    @staticmethod
    def mnoz(u1, u2):
        return u1.licznik * u2.licznik, u1.mianownik * u2.mianownik

    @staticmethod
    def dziel(u1, u2):
        return u1.licznik * u2.mianownik, u1.mianownik * u2.licznik


def main():
    Jan = Osoba("Jan", "Nowak", 48)
    Adam = Osoba("Adam", "Mickiewicz", 220)

    Jan.przedstaw_sie()
    Adam.przedstaw_sie()

    wiek_Adama_przed = Adam.urodziny()
    Adam.przedstaw_sie()
    print(f"Wiek Adama sprzed urodzin: {wiek_Adama_przed}")

    # modyfikujemy pola
    Jan.imie = "Stanislaw"
    Jan.nazwisko = "Mickiewicz"
    Jan.wiek = 133

    Jan.przedstaw_sie()

    print('\n######################################## \n')

    test = Test()
    print(test.publiczne)
    print(test._chronione)
    print(test._Test__prywatne)

    print('\n######################################## \n')

    a = Licznik()
    b = Licznik()
    c = Licznik()

    print(f"a to obiekt nr {a.ktory}")
    print(f"b to obiekt nr {b.ktory}")
    print(f"c to obiekt nr {c.ktory}")
    print(f"Liczba obiektow to: {Licznik.policz()}")
    a = None
    b = None
    print(f"Liczba obiektow to: {Licznik.policz()}")

    print('\n######################################## \n')

    f1 = FunkcjaKwadratowa(1, 5, 1)
    f1.rozwiaz()

    print('\n######################################## \n')

    z1 = Zespolona(5, 2)
    z2 = Zespolona(1, 5)

    print(z1.modul())
    print(Zespolona.dodaj(z1, z2))
    print(Zespolona.mnoz(z1, z2))

    print('\n######################################## \n')

    u1 = Ulamek(0, 4)
    u2 = Ulamek(2, 0)

    # print(u1.skroc())
    print(Ulamek.dodaj(u1, u2))
    print(Ulamek.odejmij(u1, u2))
    print(Ulamek.mnoz(u1, u2))
    try:
        print(Ulamek.dziel(u1, u2))
    except ZeroDivisionError as e:
        print(e)


if __name__ == '__main__':
    main()
