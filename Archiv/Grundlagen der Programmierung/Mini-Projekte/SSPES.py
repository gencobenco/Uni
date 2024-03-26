import random

B_Score = 0
C_Score = 0
SSPES = 0

def spielmodus():  
    global SSPES
    ans = input("Spielmodusauswahl: SSP oder SSPES?\n").lower()
    if ans in ["was", "?", "was?", "hä", "hä?"]:
        print("Schere, Stein, Papier oder auch noch mit Echse und Spock?\n")
        spielmodus()
    elif ans == "sspes":
        SSPES = 1
        return
    elif ans == "ssp":
        SSPES = 0
        return
    else:
        print("Folgende Eingaben sind möglich: SSP, SSPES oder ?")
        spielmodus()

spielmodus()

def benutzerwahl():
    if SSPES == 0:
        ans = input("Schere, Stein, Papier! Was setzt du ein?\n").lower()
    else: 
        ans = input("Schere, Stein, Papier, Echse, Spock! Was setzt du ein?\n").lower()
    if ans == "reicht":
            return None
    elif ans == "schere":
            print("Du hast Schere gewählt.")
            return "Schere"
    elif ans == "stein":
            print("Du hast Stein gewählt.")
            return "Stein"
    elif ans == "papier":
            print("Du hast Papier gewählt.")
            return "Papier"
    elif ans == "echse":
            print("Du hast Echse gewählt.")
            return "Echse"
    elif ans == "spock":
            print("Du hast Spock gewählt.")
            return "Spock"
    else:
            if SSPES == 1:
                print("Bitte gib eine von den fünfen an.")
            else:
                print("Bitte gib ein von den dreien an.")
            return benutzerwahl()
    

def computerwahl():
    if SSPES == 1:
        SSP_choice = ["Schere", "Stein", "Papier", "Echse", "Spock"]
    else:
        SSP_choice = ["Schere", "Stein", "Papier"]
    return random.choice(SSP_choice)


def ermittlung_gewinner(benutzer, computer):
    global B_Score, C_Score, SSPES

    if benutzer == "reicht":
        return None
    elif benutzer == computer:
        return "Unentschieden!\n"
    elif (benutzer == "Papier" and computer == "Stein") or (benutzer == "Stein" and computer == "Schere") or (benutzer == "Schere" and computer == "Papier"):
        B_Score += 1
        print("Du gewinnst!\n")
    elif SSPES == 1:
        if (benutzer == "Echse" and computer == "Spock") or (benutzer == "Spock" and computer == "Stein") or (benutzer == "Papier" and computer == "Spock") or (benutzer == "Spock" and computer == "Schere") or (benutzer == "Stein" and computer == "Echse") or (benutzer == "Echse" and computer == "Papier") or (benutzer == "Schere" and computer == "Echse"):
            B_Score += 1
            print("\nDu gewinnst!\n")
        else:
            C_Score += 1
            print("\nDer Computer gewinnt!\n")
    else:
        C_Score += 1
        print("Der Computer gewinnt!\n")
    return B_Score, C_Score, SSPES

if SSPES == 1: 
    print("\nWillkommen zu Schere, Stein, Papier, Echse, Spock!\n")
else:
    print("Willkommen zu Schere, Stein, Papier!\n")

while True:
    benutzer = benutzerwahl()
    computer = computerwahl()
    
    if benutzer is None:
        break

    print("\nDu wählst:", benutzer)
    print("\nDer Computer wählt:", computer)

    ergebnis = ermittlung_gewinner(benutzer, computer)
    print(ergebnis)

    B_Score, C_Score
    print(f"Aktueller Punktestand - \n Benutzer: {B_Score}\n Computer: {C_Score}\n")

   
print("\nVielen Dank fürs Spielen!")