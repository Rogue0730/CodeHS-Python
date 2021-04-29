def sunny_day():
    print("On a sunny day, sandals shows are appropraite footware.")
def rainy_day():
    print("On a rainy day, galoshes are appropriate footwear.")
def snowy_day():
    print("On a snowy day, boots are appropriate footwear.")

weather = input("What is the weather? (sunny, rainy, snowy):")

if weather == "sunny":
    sunny_day()
elif weather == "rainy":
    rainy_day()
elif weather == "snowy":
    snowy_day()
else: 
    print("Invaild input.")