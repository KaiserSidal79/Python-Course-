# 8-6 Städtenamen
def city_country(city, country):
    pair = city + ", " + country
    return pair.title()


p1 = city_country("Wien", "österreich")
p2 = city_country("berlin", "Deutschland")
p3 = city_country("Istanbul", "türkei")
print(p1, p2, p3)


# 8-7 Album finished version
def make_album():
    while True:
        prompt = "\nHello, create your own album! End this programm with 'e'!\n" \
             "artist: "
        artist = input(prompt)
        if artist == "e":
            break
        title = input("title :")
        if title == "e":
            break
        album = {"artist": artist, "title": title}
        return album

a = make_album()
print(a)

#a1 = make_album("Mert", "861")
#a2 = make_album("DC", "Drill", "7")
#print(a1, a2)

#8-8 Album aus Benutzereingaben siehe 8-7 :)

