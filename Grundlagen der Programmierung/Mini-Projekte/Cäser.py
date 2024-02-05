def caesar_verschluesselung(text, schluessel):
    verschluesselter_text = ""

    for buchstabe in text:
        if buchstabe.isalpha():  # Nur Buchstaben verschlüsseln
            start = ord('A') if buchstabe.isupper() else ord('a')
            verschluesselter_buchstabe = chr((ord(buchstabe) - start + schluessel) % 26 + start)
            verschluesselter_text += verschluesselter_buchstabe
        else:
            verschluesselter_text += buchstabe  # Sonderzeichen und Leerzeichen beibehalten

    return verschluesselter_text

def caesar_entzifferung(verschluesselter_text, schluessel):
    return caesar_verschluesselung(verschluesselter_text, -schluessel)

# Benutzereingabe für Text und Schlüssel
text = input("Gib den zu verschlüsselnden Text ein: ")
schluessel = int(input("Gib den Verschlüsselungsschlüssel (eine ganze Zahl) ein: "))

# Verschlüsselung
verschluesselter_text = caesar_verschluesselung(text, schluessel)
print("Verschlüsselter Text:", verschluesselter_text)

# Entzifferung
entschluesseltes_text = caesar_entzifferung(verschluesselter_text, schluessel)
print("Entziffert:", entschluesseltes_text)