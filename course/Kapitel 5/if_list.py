# 5-8 Hello Admin + 5-9 Keiner Benutzer ( "if users")
users = ["kaiser", "skillerz", "admin", "pawkn", "coolman"]
if users:
    for user in users:
        if user == "admin":
            print("Hello " + user + " would you like a status report?")
        else:
            print("Welcome, " + user + "!")
else:
    print("We need to find some users!")

# 5-10 Benutzernamen überprüfen

current_users = ["Gamer", "zOcker", "killer", "pro", "assasin"]
new_users = ["gamer", "zocker", "sportler", "sweater", "aim"]
nulower = [x.lower() for x in new_users]
culower = [y.lower() for y in current_users]
for nu in nulower:
    if nu in culower:
        print("This name isn't available.")
    else:
        print("This name is available.")

# 5-11 Englische Ordnungszahlen
numbers = [n for n in range(1, 10)]
for number in numbers:
    if number == numbers[0]:
        print(str(number) + "st")
    elif number == numbers[1]:
        print(str(number) + "nd")
    elif number == numbers[2]:
        print(str(number) + "rd")
    else:
        print(str(number) + "th")
