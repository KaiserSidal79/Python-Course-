# 3-4: Einladung der ersten Personen
guests = ["Irina", "Sieglinde", "Dervis"]

# 3-5 Gästeliste wird geändert
print("Der Gast " + guests[2] + " kann leider nicht erscheinen!")
guests[2] = "Oma"

# 3-6 Weitere Gäste
print("Ich habe einen größeren Esstisch gefunden, weshalb mehr Gäste "
      "eingeladen werden können!")
guests.insert(0, "Tante")
guests.insert(3, "Onkel")
guests.append("Freund")
i1 = guests[0] + " ich lade dich zum Abendessen ein!"
i2 = guests[1] + " ich lade dich zum Abendessen ein!"
i3 = guests[2] + " ich lade dich zum Abendessen ein!"
i4 = guests[3] + " ich lade dich zum Abendessen ein!"
i5 = guests[4] + " ich lade dich zum Abendessen ein!"
i6 = guests[5] + " ich lade dich zum Abendessen ein!"

# 3-7: Die Gästeliste verkleinern:
print("Ich kann den Tisch leider doch nicht benutzen!")
ausgeladen1 = guests.pop()
print(
    "Leider kannst du doch nicht kommen, " + ausgeladen1 + ". Es tut mir leid...")
ausgeladen2 = guests.pop()
print(
    "Leider kannst du doch nicht kommen, " + ausgeladen2 + ". Es tut mir leid...")
ausgeladen3 = guests.pop()
print(
    "Leider kannst du doch nicht kommen, " + ausgeladen3 + ". Es tut mir leid...")
ausgeladen4 = guests.pop()
print(
    "Leider kannst du doch nicht kommen, " + ausgeladen4 + ". Es tut mir leid...")
print(guests[0] + " du kannst kommen!")
print(guests[1] + " du kannst kommen")

# 3-9
print(len(guests))
