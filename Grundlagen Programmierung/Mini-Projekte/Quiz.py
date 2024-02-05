class Frage:
    def __init__(self, text, antwort, kategorie):
        self.text = text
        self.antwort = antwort
        self.kategorie = kategorie

    def pruefe_antwort(self, benutzerantwort):
        return benutzerantwort == self.antwort

class Fragenkatalog:
    def __init__(self):
        self.fragen = []

    def neue_frage_hinzufuegen(self, frage, antwort, kategorie):
        neue_frage = Frage(frage, antwort, kategorie)
        self.fragen.append(neue_frage)

    def frage_anzeigen(self, frage_index):
        if 0 <= frage_index < len(self.fragen):
            frage = self.fragen[frage_index]
            print(f"Kategorie: {frage.kategorie}")
            print(f"Frage: {frage.text}")
        else:
            print("Ungültige Frage-Index.")

# Beispiel der Verwendung
fragenkatalog = Fragenkatalog()
fragenkatalog.neue_frage_hinzufuegen("Was ist die Hauptstadt von Deutschland?", "Berlin", "Geografie")
fragenkatalog.neue_frage_hinzufuegen("Wie viele Kontinente gibt es auf der Erde?", "7", "Allgemeinwissen")
fragenkatalog.neue_frage_hinzufuegen("Was ist 1+1?", "2", "Mathe")
fragenkatalog.neue_frage_hinzufuegen("Welche Nummer ist die neuste PlayStation-Konsole?", "5", "Gaming")
fragenkatalog.neue_frage_hinzufuegen("Welcher Supermarkt hat den Eigenprodukt _ja!_ ", "Rewe", "Shopping")
fragenkatalog.neue_frage_hinzufuegen("Was steht für USB?", "Universal Serial Bus", "IT") 
fragenkatalog.neue_frage_hinzufuegen("Wie heißt Marc mit Nachnamen?", "Müller", "Uni")

while True:
    print("1. Frage hinzufügen")
    print("2. Quiz starten")
    print("3. Beenden")
    auswahl = input("Ihre Auswahl: ")

    if auswahl == "1":
        frage = input("Geben Sie die Frage ein: ")
        antwort = input("Geben Sie die Antwort ein: ")
        kategorie = input("Geben Sie die Kategorie ein: ")
        fragenkatalog.neue_frage_hinzufuegen(frage, antwort, kategorie)
    elif auswahl == "2":
        for i in range(len(fragenkatalog.fragen)):
            fragenkatalog.frage_anzeigen(i)
            benutzerantwort = input("Ihre Antwort: ")
            frage = fragenkatalog.fragen[i]

            if frage.pruefe_antwort(benutzerantwort):
                print("Richtig!")
            else:
                print("Falsch.")
    elif auswahl == "3":
        break
