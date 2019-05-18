class Zwierze:
    def __init__(self, wiek):
        self.wiek = wiek

    @property
    def wiek(self):
        return self.__wiek

    @wiek.setter
    def wiek(self, wiek):
        if wiek < 0:
            self.__wiek = 0
        elif wiek > 200:
            self.__wiek = 200
        else:
            self.__wiek = wiek


def main():
    jakis_zwierz = Zwierze(202)
    print(jakis_zwierz.wiek)
    jakis_zwierz.wiek = -10
    print(jakis_zwierz.wiek)
    jakis_zwierz.wiek = 30
    print(jakis_zwierz.wiek)


if __name__ == '__main__':
    main()