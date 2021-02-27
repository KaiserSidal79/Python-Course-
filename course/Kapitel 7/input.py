# 7-1 Leihwagen
car = input("Which car do you want? ")
print("Let me check if we have a " + car + "!")

# 7-2 Restaurantplätze
guests = input("How big is your group? ")
if int(guests) >= 8:
    print("Sorry, you have to wait for a bigger table!")
else:
    print("Follow me!")

# 7-3 Vielfaches von 10
prompt = "We are checking if your number is a product of 10!"
prompt += "\nType your number: "
n = input(prompt)
if int(n) % 10 == 0:
    print("True!")
else:
    print("False!")
