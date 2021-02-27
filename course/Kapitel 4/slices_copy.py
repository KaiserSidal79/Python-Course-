#4-10 slices: siehe nummeric... in 4-6
#4-11 Pizza siehe 4-1
#4-12 foods mit weiteren Schleifen
my_foods = ["sucuk", "döner", "burger", "cigköfte"]
friend_foods = my_foods[:]
friend_foods.append("nudeln")
my_foods.insert(0, "pastirma")
for mf in my_foods:
    print(mf)
for ff in friend_foods:
    print(ff)