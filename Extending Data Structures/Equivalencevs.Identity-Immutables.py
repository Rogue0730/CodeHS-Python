"""
This program displays equivalence and identity with immutables.
"""

string_one = "hi there"
string_two = string_one

if string_one == string_two:
    print "Equivalent!"
else:
    print "Not equivalent."

if string_one is string_two:
    print "Identical!"
else:
    print "Not identical."