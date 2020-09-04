"""
Python exposes a terse and intuitive syntax for performing 
slicing on lists and strings. This makes it easy to reference
only a portion of a list or string. 

This Stack Overflow answer provides a brief but thorough
overview: https://stackoverflow.com/a/509295

Use Python's slice syntax to achieve the following:
"""

a = [2, 4, 1, 7, 9, 6]

# Output the second element: 4:
elem4 = slice(1)
print(a[elem4])

# Output the second-to-last element: 9
elem9 = slice(4, 5)
print(a[elem9])

# Output the last three elements in the array: [7, 9, 6]
last4 = slice(2, 6)
print(a[last4])

# Output the two middle elements in the array: [1, 7]
middle = slice(2, 4)
print(a[middle])

# Output every element except the first one: [4, 1, 7, 9, 6]
allBut1st = slice(1, 6)
print(a[allBut1st])

# Output every element except the last one: [2, 4, 1, 7, 9]
allButLast = slice(0, 5)
print(a[allButLast])

# For string s...

s = "Hello, world!"

# Output just the 8th-12th characters: "world"
world = slice(7, 12)
print(s[world])