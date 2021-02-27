#5-1 Bedingungen

car ="VW"
print("Is car == 'VW'? I predict True.")
print(car=="VW")

print("\nIs car = 'Audi'? I predict False.")
print(car=="Audi")

#weitere 10
#5-2 Noch mehr Bedingungen
string1 = "Mert"
string2 = "mert"
if string1.lower() == string2:      #erwitert mit lower()
    print("equal")
else:
    print("different")

# connected:
x= 27
y= 24
z= 25
print(x<y<z)
if x < z and y < z or x != z:
    print("yessir")
else:
    print("nope")

cars = ["Audi", "Porsche", "Ferrari", "BMW"]
print("Audi" in cars)
print("Mercedes" not in cars)