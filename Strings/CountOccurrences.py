def count_occurrences(name, letter):
    counter = 0
    for checker in name:
        if(checker == letter):
            counter+=1
    return counter

word = input("Enter a word: ")
letter = input("Enter a letter: ")

print (count_occurrences(word, letter))