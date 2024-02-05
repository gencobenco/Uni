ans = input("Willst du begrüßt werden? Ja/Nein?").lower()
if ans == "ja":
    zeit = int(input("Wieviel Uhr ist es? Gib nur die Stunde an: "))
    if 0 <= zeit < 24:
        if zeit in range(5, 12):
            zeit = "Guten Morgen, "
        elif zeit in range(12, 19):
            zeit = "Guten Mittag, "
        elif zeit in range(18, 24) or zeit in range(0, 6):
            zeit = "Guten Abend, "
        else:
            print("error")
            zeit = ""

        name = input("Wie heißt du denn? ").capitalize()
        print(zeit + name + "!")
        
    else:
        print("Ungültige Eingabe. Bitte gib eine Stunde zwischen 0 und 23 an.")
else:
    print("Schade :(")