def fahrenheit_to_celcius(fahrenheit):
    return (fahrenheit - 32) / 1.8
# Now write your function for converting Fahrenheit to Celsius.
def celcius_to_fahrenheit(celcius):
    return celcius * 1.8 + 32
#ask te user to enter a temperature
try:
    temperature = int(input("Enter a temp: "))
except ValueError:
    print("That wasn't an integer.")
    
# Now change 0C to F:
print ("0C In F: " + str(celcius_to_fahrenheit(0)))
# Change 100C to F:
print ("100C In F: " + str(celcius_to_fahrenheit(100)))
# Change 40F to C:
print ("40F In C: " + str(fahrenheit_to_celcius(40)))
# Change 80F to C:
print ("80F In C: " + str(fahrenheit_to_celcius(80)))