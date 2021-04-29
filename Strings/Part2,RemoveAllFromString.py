def remove_all_from_string(string1, string2):
    if not string2:
        return string1
    while True:
        index = string1.find(string2)
        if index == -1:
            return string1
        string1 = string1[:index] + string1[index + len(string2):]
        
print remove_all_from_string("bananas", "a")
print remove_all_from_string("bananas", "na")