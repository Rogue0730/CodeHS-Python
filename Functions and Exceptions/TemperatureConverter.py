# Write your function for converting Celsius to Fahrenheit here.
# Make sure to include a comment at the top that says what
# each function does!
def convert_c(y):
    f = (1.8 * y) + 32
    return f
# Now write your function for converting Fahrenheit to Celsius.
def convert_f(x):
    c = (x - 32) // 1.8
    return c
    
# Now change 0C to F:
convert_c(0)

# Change 100C to F:
convert_c(100)


# Change 40F to C:
convert_f(40)


# Change 80F to C:
convert_f(80)