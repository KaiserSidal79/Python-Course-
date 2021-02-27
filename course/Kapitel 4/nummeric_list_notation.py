#4-3 bis 20 zählen (ähnlich zu 4-4 wird zu 1 Mio. erweitert)
#for value in range(1,1000001):
    #print(value)

#4-5 Summe von 1 bis 1000000
summio = list(range(1,1000001))
print(min(summio))
print(max(summio))
print(sum(summio))

#4-6 ungerade Zahlen
uneven_numbers = list(range(1,21,2))
for un in uneven_numbers:
    print(un)

#4-10
print("First three items uneven numbers: ")
for unnu in uneven_numbers[:3]:
    print(unnu)

print("Middle three items uneven numbers: ")
for unnu2 in uneven_numbers[4:7]:
    print(unnu2)

print("Last three items uneven numbers: ")
for unnu3 in uneven_numbers[-3:]:
    print(unnu3)

#4-7 vielfachen von 3
three = [print(3*v) for v in range(1,11)]

#4-8 Kubikzahlen in #3-9 Version
cubic = [print(c**3) for c in range(1,11)]