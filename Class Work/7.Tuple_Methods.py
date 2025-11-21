# A tuple is an immutable, ordered collection of elements.

# Empty Tuple
empty_tuple = ()

# Single-element Tuple (note the trailing comma)
single_tuple = (5,)

# Multi-element Tuple
my_tuple = (1, "apple", 3.5)

# Without parentheses (implicit tuple creation)
new_tuple = 1, 2, 3
print(new_tuple)
print(type(new_tuple))  # <class 'tuple'>

# String Tuple Examples
str_tuple = ("Yuva", "Teja", "Python", "Developer")
print(str_tuple)
print(type(str_tuple))  # <class 'tuple'>

# Tuple with repeated strings
str_tuple2 = ("apple", "banana", "apple", "cherry")
print(str_tuple2)


# 2. Accessing Tuple Elements:

# Positive Indexing:
my_tuple = (10, 20, 30, 40)
print(my_tuple[2])  # Output: 30

# Negative Indexing
my_tuple = (10, 20, 30, 40)
print(my_tuple[-1])  # Output: 40

# Slicing:
print(my_tuple[0:2])  # Output: (10, 20)


# 3. Operations on Tuples

tuple1 = (1, 2, 3, 4)
tuple2 = ("M", "X", "L", "XL")

combined_tuple = tuple1 + tuple2
print(combined_tuple)  # Output: (1, 2, 3, 4, 'M', 'X', 'L', 'XL')

# Repetition:
print(tuple1 * 3)
# Output: (1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4)

# Membership operator:
print(2 in tuple1)  # True

# Tuple unpacking:
a, b, c, d = tuple1
print(a, b, c, d)  # Output: 1 2 3 4


# String Tuple Unpacking
str_tup3 = ("Hello", "Yuva", "Welcome")
x, y, z = str_tup3
print(x, y, z)


# Tuple Methods:

tuple33 = (1, 2, 3, 4, 4, 34, 2, 2, 2, 4, 2, 2, 4)
print(tuple33)

# count:
print(tuple33.count(2))  # 6

# index:
print(tuple33.index(4))  # 3

# len:
print(len(tuple33))  # 13

# max & min:
print(max(tuple33))  # 34
print(min(tuple33))  # 1

# Iterable to Tuple:
new_tup = tuple([1, 2, 3, 54, 3, 5])
print(new_tup)  # (1, 2, 3, 54, 3, 5)

# Iterable String to Tuple Example:
str_to_tuple = tuple("PYTHON")
print(str_to_tuple)  # ('P', 'Y', 'T', 'H', 'O', 'N')
