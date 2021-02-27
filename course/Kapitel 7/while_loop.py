# 7-4 Pizzabeläge
active = True
while active:
    belag = input("Stoppe mit Hilfe von 'quit'\nWähle einen Belag: ")
    if belag == "quit":
        active = False
    else:
        print(
            "Der Belag " + belag.title() + " wurde deiner Pizza hinzugefügt!")

# 7-5 Eintrittskarten
while True:
    guest = input("How old are you? ")
    if guest == "quit":
        break
    elif int(guest) <= 3:
        print("Your ticket costs: 0€")
    elif int(guest) <= 12:
        print("Your ticket costs: 10€")
    else:
        print("Your ticket costs: 15€")

# 7-6 Endlosschleife
x = 0
while x < 5:
    print(x)
