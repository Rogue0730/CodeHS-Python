role = input("Are you an administrator, teacher, or student?: ")

if role == "administrator" or role == "teacher":
    print("Administrators and teachers get keys!")
elif role == "student":
    print("Students do not get keys!")
else:
    print("You can only be an administrator, teacher, or student!")