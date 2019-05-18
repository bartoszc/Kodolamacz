try:
    f = open(sciezka_do_pliku)
    print(2/0)
    print(f.read())
except ZeroDivisionError as e:
    print(e)
finally:
    f.close()

########################################3

try:
    with open(sciezka_do_pliku) as f:
        print(f.read())
        print(2/0)
except ZeroDivisionError as e:
    print(e)