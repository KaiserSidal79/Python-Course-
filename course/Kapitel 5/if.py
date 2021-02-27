#5-3 Farben von feindlichen Raumschiffen: (1)
alien_color = "red"
points3 = 0
if alien_color == "green":
    points3 += 5

print("Your score: "+str(points3))

#5-4 (2)
points4 = 0
if alien_color == "green":
    points4 += 5
else:
    points4 += 10

print("Your score: "+str(points4))

#5-5 (3)
points5 = 0
if alien_color == "green":
    points5 += 5
elif alien_color == "yellow":
    points5 += 10
elif alien_color == "red":
    points5 += 15

print("Your score: "+str(points5))

#5-6 Altersstufen
age = 17
if age < 2:
    print("You are a baby!")
elif age >= 2 and age < 4:
    print("You are a little kid!")
elif age >= 4 and age < 13:
    print("You are a kid!")
elif age >= 13 and age < 20:
    print("You are a teenager!")
elif age >= 20 and age < 65:
    print("You are an adult!")
else:
    print("You are a pensioner!")

#5-7 Lieblingsobst
favorite_fruits = ["Birne", "Ananas", "Erdbeere"]
if "Birne" in favorite_fruits:
    print("Mert mag Birne")
if "Apfel" in favorite_fruits:
    print("Mert mag Apfel")
if "Erdbeere" in favorite_fruits:
    print("Mert mag Erdbeere")
if "Ananas" in favorite_fruits:
    print("Mert mag Ananas")
if "Kirsche" in favorite_fruits:
    print("Mert mag Kirsche")