# 8-3 T-Shirt
def make_shirt(size="L", text="I love Python"):
    print("The shirt in size " + size.upper() + " reads: " + text)


make_shirt("l", "Barsport")
make_shirt("m")
make_shirt(size="M", text="Sportler")
make_shirt()


# 8-4 Große T-Shirts siehe 8-3

# 8-5 Städte
def describe_city(city, country="germany"):
    print(city.title() + " is located in " + country)


describe_city("berlin")
describe_city("munich")
describe_city("vienna", "austria")
