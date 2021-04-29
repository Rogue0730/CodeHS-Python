def remove_all_from_string(string1, string2):
    while True:
        index = string1.find(string2)
        if index == -1:
            return string1
        string1 = string1[:index] + string1[index+1:]

print remove_all_from_string("hello", "l")