# lambda is a small anonymous function — a function without a regular name, written in a single expression.

cube = lambda x: x ** 3
another_cube = cube(2)
print(another_cube)

# lambda is keyword
# we can only pass the reference to another varible but cannot pass the value
# e.g: another_cube = cube() X, another_cube = cube