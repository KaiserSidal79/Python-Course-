# 7-8 Sandwiches
sandwich_orders = ["Salami", "Sucuk", "Käse", "Salat", "Pastirma", "Fisch",
                   "Pastirma", "Pastirma"]
finished_sandwiches = []

while sandwich_orders:
    while "Pastirma" in sandwich_orders:
        print("Sorry Pastirma is out of order!")
        sandwich_orders.remove("Pastirma")
    current_sandwich = sandwich_orders.pop()
    print("I made your " + current_sandwich + " Sandwich!")
    finished_sandwiches.append(current_sandwich)
print("\nMade sandwiches: ")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)

# 7-9 kein Pastirma siehe oben

# 7-10 Traumurlaub
destinations = {}
polling_active = True
while polling_active:
    name = input("Hey, what is your name? ")
    destination = input("Ok " + name + " where you would love travelling to? ")
    destinations[name] = destination
    repeater = input("Do you have another possible attendent? yes/no: ")
    if repeater == "no":
        polling_active = False
print("\nPolling Results:")
for n, d in destinations.items():
    print(n + " wants to travel to " + d + "!")
