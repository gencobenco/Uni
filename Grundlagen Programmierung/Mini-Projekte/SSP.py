import random

B_Score = 0
C_Score = 0

def benutzerwahl():
    ans = input("Schere, Stein, Papier! Was setzt du ein? ").lower()
    
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
    else:
        print("Bitte gib eine von den dreien an.")
        return benutzerwahl()
    

def computerwahl():
    SSP_choice = ["Schere", "Stein", "Papier"]
    return random.choice(SSP_choice)


def ermittlung_gewinner(benutzer, computer):
    global B_Score, C_Score

    if benutzer == "reicht":
        return None
    elif benutzer == computer:
        return "Unentschieden!\n"
    elif (benutzer == "Papier" and computer == "Stein") or (benutzer == "Stein" and computer == "Schere") or (benutzer == "Schere" and computer == "Papier"):
        B_Score += 1
        print("Du gewinnst!\n")
    else:
        C_Score += 1
        print("Der Computer gewinnt!\n")
    
    return B_Score, C_Score

print("Willkommen zu Schere, Stein, Papier!")

while True:
    benutzer = benutzerwahl()
    computer = computerwahl()

    if benutzer is None:
        break

    print("\nDu wählst:", benutzer)
    print("Der Computer wählt:", computer)

    ergebnis = ermittlung_gewinner(benutzer, computer)
    print(ergebnis)

    B_Score, C_Score
    print(f"Aktueller Punktestand - \n Benutzer: {B_Score}\n Computer: {C_Score}")

   
print("\nVielen Dank fürs Spielen!")