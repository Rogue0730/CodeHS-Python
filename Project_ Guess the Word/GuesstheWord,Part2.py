secret_word = "word"
dashes = '-' * len(secret_word)


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
               
def put_pashes(word, dashes, guess):
    for i in range(len(word)):
        if word[i] == guess:
            dashes = dashes[:i] + guess + dashes[i + 1:]
    return dashes
    

while True:
    print(dashes)
    guess = get_guess()
    dashes = put_pashes(secret_word, dashes, guess)
    if guess in secret_word:
        print("That letter is in the secret word!")
    else:
        print("That letter is not in the secret word.")