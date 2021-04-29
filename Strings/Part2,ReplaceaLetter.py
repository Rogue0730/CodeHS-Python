def replace_at_index(txt, ind, let):
    new_txt = ""
    for x in range(len(txt)):
        if x == ind:
            new_txt += let
        else:
            new_txt += txt[x]
    return new_txt


print(replace_at_index(input("Enter a word or phrase: "), int(input("Enter an index value: ")), input("Enter the new letter: ")))