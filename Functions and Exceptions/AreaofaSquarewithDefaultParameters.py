def calculate_area(side_length = 10):
    area = side_length * side_length
    print("The area of a square with side of length " + str(side_length) + " is " + str(area))

side_length1 = int(input("Enter side length: "))

if side_length1 <= 0:
    calculate_area()
else:
    calculate_area(side_length1)