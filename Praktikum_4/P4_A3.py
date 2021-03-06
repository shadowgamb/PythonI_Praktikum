def count_words(liste_mit_sachen):
    #Alle vorhandenen Elemente in Strings umwandeln
    liste_mit_sachen = [str(woerter) for woerter in liste_mit_sachen]
    gezaehlte_woerter = {words:liste_mit_sachen.count(words) for words in liste_mit_sachen}
    return gezaehlte_woerter

def count_capital_words(*woerter_zu_zaehlen):
    #Liste erstellen und alles in Strings umwandlen
    woerter_zu_zaehlen = list(str(woerter) for woerter in woerter_zu_zaehlen)
    #Leerzeichen entfernen
    woerter_zu_zaehlen = [zeichen.strip() for zeichen in woerter_zu_zaehlen]
    #If-Anweisung für Großbuchsten und im Alphabet vorhanden
    woerter_zu_zaehlen = [zeichen for zeichen in woerter_zu_zaehlen if zeichen.istitle() and zeichen[0].isalpha()]
    #ALle Wörter zählen
    woerter_zu_zaehlen = count_words(woerter_zu_zaehlen)
    return woerter_zu_zaehlen


assert count_capital_words(3, ".Hello", "Hello", " world", ",", "    Python", "  Python ", 5+3j, "Hello.") \
        == {"Hello": 1, "Python": 2, "Hello.": 1}
assert count_capital_words("A", "b", "a_B") == {"A": 1}
assert count_capital_words(1, 2, 3) == {}
assert count_capital_words({1}) == {}
assert count_capital_words("_U", "I_") == {"I_": 1}
assert count_capital_words() == {}