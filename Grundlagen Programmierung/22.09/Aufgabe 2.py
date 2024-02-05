hp = int(input("Höchstpunktzahl? :"))

p = int(input("Punktzahl? :"))

if hp <= 0:
    print("Höchstpunktzahl muss über 0 sein")

elif p >= hp / 6 * 5:
    print("A")

elif p >= hp / 6 * 4:
    print("B")

elif p >= hp / 6 * 3:
    print("C")

elif p >= hp / 6 * 2:
    print("D")

elif p >= hp / 6:
    print("E")

elif p < hp / 6:
    print("F")



