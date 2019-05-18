def sprytne_potegowanie(podstawa, wykladnik):
    if wykladnik == 0:
        return 1
    return podstawa * sprytne_potegowanie(podstawa, wykladnik-1)


def czy_palindrom(napis):
        return napis == napis[::-1]


def czy_anagram(word1, word2):
    flag = True
    s = {}
    for letter in word1:
        s.setdefault(letter, 0)
        s[letter] += 1

    for letter in word2:
        if letter in s.keys() and s[letter] >= 1:
            s[letter] -= 1
            if s[letter] == 0:
                del s[letter]
        else:
            flag = False
            break
    return flag


def moda(lista):
    s = {}
    for i in lista:
        s.setdefault(i, 0)
        s[i] += 1
    return max(s.keys(), key=(lambda k: s[k]))


if __name__ == '__main__':
    print("2^10 = " + str(sprytne_potegowanie(2, 10)))
    print("czyPalindrom(kajak) = " + str(czy_palindrom("kajak")))
    print("czyPalindrom(kobyla) = " + str(czy_palindrom("kobyla")))
    print("czyPalindrom2(kajak) = " + str(czy_palindrom("kajak")))
    print("czyPalindrom2(kobyla) = " + str(czy_palindrom("kobyla")))
    print("czyAnagram(kajak, jaakk) = " + str(czy_anagram("kajak", "jaakk")))
    print("czyAnagram(kobyla, boczek) = " + str(czy_anagram("kobyla", "boczek")))
    print("moda([1,6,4,7,2,8,6,7,6]) = " + str(moda([1, 6, 4, 7, 2, 8, 6, 7, 6])))





