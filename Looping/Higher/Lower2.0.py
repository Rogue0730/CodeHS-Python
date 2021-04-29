my_float = 3.3312

while True:
    guessed_num = float(input("Guess a number: "))
    if round(guessed_num, 2) > round(my_float, 2):
        print("Too High!")
    elif round(guessed_num, 2) < round(my_float, 2):
        print("Too Low!")
    else:
        print("Correct!")
        break