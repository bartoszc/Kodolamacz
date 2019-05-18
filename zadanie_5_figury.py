from abc import ABC, abstractmethod
import math


class Figura(ABC):
    def __init__(self, a):
        self.a = a

    @abstractmethod
    def nazwa(self):
        pass

    def wypisz(self):
        print(f'Jestem {self.nazwa()}. Moj obwod to {self.obwod()}. Moje pole to: {self.pole()}')

    @abstractmethod
    def obwod(self):
        pass

    @abstractmethod
    def pole(self):
        pass


class Kolo(Figura):
    def nazwa(self):
        return 'Kolo'

    def obwod(self):
        return 2 * math.pi * self.a

    def pole(self):
        return math.pi * (self.a ** 2)


class Kwadrat(Figura):
    def nazwa(self):
        return 'Kwadrat'

    def pole(self):
        return self.a * self.a

    def obwod(self):
        return 4 * self.a


class Prostokat(Kwadrat):
    def nazwa(self):
        return 'Prostokat'

    def __init__(self, a, b):
        super().__init__(a)
        self.b = b

    def pole(self):
        return self.a * self.b

    def obwod(self):
        return 2*self.a + 2*self.b


class Trojkat(Prostokat):
    def nazwa(self):
        return 'Trojkat'

    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.c = c

    def pole(self):
        return self.a / 2 * self.b

    def obwod(self):
        return self.a + self.b + self.c


def oblicz_wszystko(figury):
    for fig in figury:
        fig.wypisz()


def main():
    k1 = Kolo(5)
    kw1 = Kwadrat(5)
    pr1 = Prostokat(5, 10)
    tr1 = Trojkat(5, 10, 2)

    figury = [k1, kw1, pr1, tr1]
    oblicz_wszystko(figury)


if __name__ == "__main__":
    main()

