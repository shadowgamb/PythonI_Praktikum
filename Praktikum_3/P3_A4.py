# Lösen Sie Aufgabe 3 in dieser Zelle
L1 = ['P', 3, 'y', 't', 0.0, 'h', 1, 1, 1.0, 'o', 'n' ]
L2 = ['A', 6, 8.3, 'n', 5, 'n', 'a']
L3 = ['P', 'y', 't', 'h', 'o', 'n']

def cleaner(zu_reinigen):

    # woerter_zu_zaehlenn für die neue gereinigte Liste und die Länge zum Durchlaufen der Liste
    gereinigte_liste = []
    laenge = len(zu_reinigen)

    # For-Schleife zum Aussortieren der Strings und um an die neue Liste anzuhängen
    for i in range(0, laenge):
        if isinstance(zu_reinigen[i], str):
            gereinigte_liste.append(zu_reinigen[i].lower())

    return gereinigte_liste

def palindrome(liste):

    # Aufruf der Cleaner-Funktion
    gereinigt = cleaner(liste)

    # umgedreht für das umkehren der liste fürs Palindrom
    umgedreht = list(reversed(gereinigt))
    wort = ''.join(gereinigt)

    return (wort.capitalize(), umgedreht==gereinigt)

assert palindrome(L1) == ('Python', False)
assert palindrome(L2) == ('Anna', True)
assert palindrome(L1) == palindrome(L3)
assert L1 == ['P', 3, 'y', 't', 0.0, 'h', 1, 1, 1.0, 'o', 'n' ]
assert L2 == ['A', 6, 8.3, 'n', 5, 'n', 'a']