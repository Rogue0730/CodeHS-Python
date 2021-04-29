def replace_at_index(txt, ind):
    new_txt = ""
    for x in range(len(txt)):
        if x == ind:
            new_txt += "-"
        else:
            new_txt += txt[x]
    return new_txt


print(replace_at_index("eggplant", 3))