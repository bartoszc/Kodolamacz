def main():
    r = 't'
    while r == 't':
        print('Podaj w oddzielnych wierszach liczbę, operację matematyczną: +,-,*,/,%, a następnie kolejną liczbę:')
        try:
            n1 = float(input())
            f = input()
            n2 = float(input())
        except ValueError:
            print('Podałeś błędne wartości!')
            continue
        if f == '+':
            print('Twoj wynik to:', n1+n2)
        elif f == '-':
            print('Twoj wynik to:', n1-n2)
        elif f == '*':
            print('Twoj wynik to:', n1*n2)
        elif f == '/':
            try:
                print('Twoj wynik to:', n1 / n2)
            except ZeroDivisionError:
                print('Nie mozna dzielic przez 0!')
        elif f == '%':
            print('Twoj wynik to:', n1 % n2)
        else:
            print('Brak operacji w zasobach')
            continue

        r = input('Chcesz wykonac kolejne dzialanie? Wpisz litere t lub n.')
        if r == 't':
            continue
        elif r == 'n':
            break
        else:
            print('Niezrozumiała komenda')
            r = input('Chcesz wykonac kolejne dzialanie? Wpisz litere t lub n.')


if __name__ == '__main__':
    main()
