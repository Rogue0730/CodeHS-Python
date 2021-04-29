def vowels(x):
    name = user_name.lower()
    if name.find(x) != -1:
        print("There is an " + x + " in you name, found at index " + str(name.find(x)))


user_name = input("What is yur first name?: ")

vowels("a")
vowels("i")
vowels("e")
vowels("u")
vowels("o")