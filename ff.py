import math

class Ulamek:
  def __init__(self, licznik, mianownik):
    if mianownik == 0:
      raise ZeroDivisionError("Mianownik równy zero.")
    self.licznik = licznik
    self.mianownik = mianownik

  def wypisz(self):
    print(f"({self.licznik})/({self.mianownik})")

  def skroc(self):
    nwd = math.gcd(self.licznik, self.mianownik)
    self.licznik //= nwd
    self.mianownik //= nwd

  @staticmethod
  def dodaj(u1, u2):
    lewy_licznik = u1.licznik * u2.mianownik
    prawy_licznik = u2.licznik * u1.mianownik
    wynik = Ulamek(lewy_licznik + prawy_licznik, u1.mianownik * u2.mianownik)
    wynik.skroc()
    return wynik

  @staticmethod
  def odejmij(u1, u2):
    lewy_licznik = u1.licznik * u2.mianownik
    prawy_licznik = u2.licznik * u1.mianownik
    wynik = Ulamek(lewy_licznik - prawy_licznik, u1.mianownik * u2.mianownik)
    wynik.skroc()
    return wynik

  @staticmethod
  def mnoz(u1, u2):
    wynik = Ulamek(u1.licznik * u2.licznik, u1.mianownik * u2.mianownik)
    wynik.skroc()
    return wynik

  @staticmethod
  def dziel(u1, u2):
    wynik = Ulamek(u1.licznik * u2.mianownik, u1.mianownik * u2.licznik)
    wynik.skroc()
    return wynik


def main():
  u1 = Ulamek(0, 4)
  u2 = Ulamek(5, 0)  # nieskrocony

  try:
    u3 = Ulamek.dziel(u2, u1)
  except ZeroDivisionError as e:
    print(e)

if __name__ == "__main__":
  main()
