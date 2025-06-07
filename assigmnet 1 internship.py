n = 5  # Number of rows

# Lower Triangular
print("Lower Triangular Pattern:")
for i in range(1, n+1):
    print("* " * i)

# Upper Triangular
print("\nUpper Triangular Pattern:")
for i in range(n, 0, -1):
    print("* " * i)

# Pyramid Pattern
print("\nPyramid Pattern:")
for i in range(1, n+1):
    print(" " * (n - i) + "* " * i)
