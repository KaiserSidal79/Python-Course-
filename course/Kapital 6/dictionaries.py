# 6-1 Person
Mert = {
    "first_name": "Mert",
    "last_name": "Sidal",
    "city": "Augsburg"
}
print("Merts informations:\n" + str(Mert))

# 6-2 Lieblingszahlen
favourite_numbers = {
    "Mert": "79",
    "Tim": "14",
    "Irina": "6",
    "Paul": "777",
    "Leo": "57"
}
for number in favourite_numbers:
    print(number + ": " + favourite_numbers[number])

# 6-3 Glossar
glossar = {
    "del": "löscht ein Objekt in einem Dictionary",
    "append": "fügt ein Objekt ans Ende einer Liste hinzu",
    "pop": "schneidet das letzte Objekt einer Liste aus",
    "sort": "sortiert eine Liste",
    "title": "macht den ersten Buchstaben des Strings groß",
    #6-4 i just add one pair
    "set": "gives back a string once"
}
for w, m in glossar.items():
    print(w + ": " + m + "\n")
