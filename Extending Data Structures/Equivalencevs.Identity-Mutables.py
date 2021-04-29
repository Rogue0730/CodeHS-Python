"""
This program shows the difference between equivalence and identity with mutables.
"""

print "---- list_two = list_one ----"
list_one = [1, 2, 3]
list_two = list_one

# Both variables now refer to the same list
if list_one == list_two:
    print "Equivalent!"
else:
    print "Not equivalent."

if list_one is list_two:
    print "Identical!"
else:
    print "Not identical."


# Altering listOne also alters listTwo
list_one[0] = 10
print "list_one: " + str(list_one)
print "list_two: " + str(list_two)

# However, replacing the contents of listOne does not affect listTwo
print "---- list_one = [1, 2, 3] ----"
list_one = [1, 2, 3]
print "list_one: " + str(list_one)
print "list_two: " + str(list_two)

if list_one == list_two:
    print "Equivalent!"
else:
    print "Not equivalent."

if list_one is list_two:
    print "Identical!"
else:
    print "Not identical."