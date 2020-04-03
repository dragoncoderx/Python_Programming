'''

Demonstrate how to:

    1) Convert an int to a float
    2) Convert a float to an int
    3) Perform floor division using a float and an int.
    4) Use two user inputted values to perform multiplication.

    Take note of what information is lost when some conversions take place.

'''

x = 1
float_version = float(x)
print(float_version)

int_version = int(float_version)
print(int_version)

y = 100//2.5
print(y)

result = int(input("type some number here: ")) * int(input("type some other number here: "))
print(result)

#done