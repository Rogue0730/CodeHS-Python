def get_guess():
    while True:
        guess = input("Guess: ")
        if isinstance(guess, int):
            print("Your guess must be a lowercase latter!")
        else:
            if guess.islower():
                if len(guess) == 1:
                    return guess
                else:
                    print("Your guess must have exactly one character!")
                    
secret_word = "word"

while True:
    guess = get_guess()
    if guess in secret_word:
        print("That letter is in the secret word!")
    else:
        print("That letter is not in the secret word.")