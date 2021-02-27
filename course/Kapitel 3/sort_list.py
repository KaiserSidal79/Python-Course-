#3-8 Weltreise
places = ["dubai", "wien", "berlin", "istanbul", "paris"]
print(places)
print(sorted(places))
print(sorted(places, reverse=True))
places.reverse()
print(places)
places.reverse()
places.sort()
print(places)
places.sort(reverse=True)
print(places)

#3-9 siehe in list_changes (Länge einer Liste)

#3-10
languages = ["Java","Python","C", "HTML", "CSS"]
print(languages)
del languages[2]
print(sorted(languages, reverse=True))
languages.append("C#")
print(sorted(languages))
bad = languages.pop()
print(bad+" isn't mine!")
languages.sort()
print(languages)
print(len(languages))
