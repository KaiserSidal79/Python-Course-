#4-1 Pizzas
pizzas = ["sucuk", "salami", "pilze"]
for pizza in pizzas:
    print("I like "+pizza.title()+"-Pizza.\n")
print("I really like Pizza!")

#4-11
friend_pizzas = pizzas[:]
pizzas.append("hawai")
friend_pizzas.append("peperoni")
print("My favourite pizzas are:")
for p1 in pizzas:
    print(p1)
print("\nMy friends favourite pizzas are:")
for p2 in friend_pizzas:
    print(p2)



#4-2 Tiere (siehe 4-1)
