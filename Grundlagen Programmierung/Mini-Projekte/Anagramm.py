def ist_anagramm(zeichenkette1, zeichenkette2):
    # Leerzeichen entfernen und in Kleinbuchstaben umwandeln, um eine
    # Fall-unspezifische Vergleich durchzuführen
    zeichenkette1 = zeichenkette1.replace(" ", "").lower()
    zeichenkette2 = zeichenkette2.replace(" ", "").lower()

    # Überprüfen, ob die sortierten Buchstaben beider Zeichenketten gleich sind
    return sorted(zeichenkette1) == sorted(zeichenkette2)

# Beispiel-Nutzung:
wort1 = "listen"
wort2 = "silent"

if ist_anagramm(wort1, wort2):
    print(f"{wort1} und {wort2} sind Anagramme.")
else:
    print(f"{wort1} und {wort2} sind keine Anagramme.")
