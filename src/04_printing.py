"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string 
method, and by using f-strings.
"""

x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"
print('%2d is 10, %1.2f is 2.25, %s is "I like turtles!"' %(x, y, z))
# Use the 'format' string method to print the same thing
print('{0:2d} is 10, {1:1.2f} is 2.25, {2:s} is "I like turtles!"'.format(x, y, z))
# Finally, print the same thing using an f-string
print(f'{x:2d} is 10, {y:1.2f} is 2.25, {z:s} is "I like turtles!"')
