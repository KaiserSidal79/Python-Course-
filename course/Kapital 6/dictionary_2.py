# 6-4 see in 6-3 (for loop)

# 6-5 Flüsse
rivers = {
    "nile": "egypt",
    "lech": "germany",
    "donau": "austria"
}
for k, v in rivers.items():
    print("The " + k.title() + " runs through " + v.title() + ".")

for river in rivers.keys():
    print(river.title())
for country in rivers.values():
    print(country.title())

# 6-6 Umfrage
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python"
}
needed_people = ["jen", "sarah", "edward", "phil", "mert", "tim", "irina",
                 "paul"]
for n in needed_people:
    if n in favorite_languages.keys():
        print("Thank you " + n.title() + "!")
    else:
        print(n.title() + ", you have to do the poll!")
