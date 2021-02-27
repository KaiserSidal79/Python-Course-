# 6-7 Menschen
Mert = {
    "first_name": "Mert",
    "last_name": "Sidal",
    "city": "Augsburg"
}
Irina = {
    "first_name": "Irina",
    "last_name": "Sidal",
    "city": "Augsburg"
}
Tim = {
    "first_name": "Tim",
    "last_name": "Dirr",
    "city": "Augsburg"
}
people = [Mert, Irina, Tim]
for p in people:
    full_name = p["first_name"] + " " + p["last_name"]
    location = p["city"]
    print(full_name + " lives in " + location + ".")
    # or just print(p)

# 6-8 Haustiere

Mylo = {
    "Art": "Hund",
    "Besitzer": "Irina"
}
Heinzi = {
    "Art": "Katze",
    "Besitzer": "Tim"
}
Speedy = {
    "Art": "Hamster",
    "Besitzer": "Mert"
}
pets = [Mylo, Heinzi, Speedy]
for pet in pets:
    print(pet["Besitzer"] + " has a " + pet["Art"] + ".")
    # or just print(pet)

# 6-9 Lieblingsplätze
favorite_places = {
    "Mert": ["Wien", "Istanbul", "Berlin"],
    "Irina": ["Wien", "Italien"],
    "Tim": ["Deutschland"]
}
# print(favorite_places)
for friend, places in favorite_places.items():
    if len(places) > 1:
        print(friend.title() + "'s favourite places are:")
        for place in places:
            print("\t" + place)
    else:
        print(friend.title() + "'s favourite place is " + places[0])
# 6-10 Lieblingszahlen
favourite_numbers = {
    "Mert": [79, 66],
    "Tim": [14, 7],
    "Irina": [6, 9, 56],
    "Paul": [777],
    "Leo": [9, 88]
}
for name, numbers in favourite_numbers.items():
    if len(numbers) > 1:
        print(name + "'s favourite numbers are:")
        for number in numbers:
            print("\t" + str(number))
    else:
        print(name + "'s favourite number is " + str(numbers[0]))
# 6-11 Städte
cities = {
    "wien": {
        "country": "austria",
        "population": "2000000",
        "fact": "The donau runs through it"
    },
    "berlin": {
        "country": "germany",
        "population": "3000000",
        "fact": "It is the capital of germany"
    },
    "istanbul": {
        "country": "turkey",
        "population": "20000000",
        "fact": "It was once calles Konstantinopel"
    }
}
for city, infos in cities.items():
    print(city.title() + ": ")
    for category, content in infos.items():
        print("\t" + category.title() + ": " + content)
# 6-12 Erweiterungen allready done
