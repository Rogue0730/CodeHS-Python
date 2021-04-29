magic_number = 3

# Your code here...
while True:
    guessed_num = int(input("Guess a number: "))
    if guessed_num > magic_number:
        print("Too High!")
    elif guessed_num < magic_number:
        print("Too Low!")
    else:
        print("Correct!")
        break