# A set is an unordered, mutable collection of unique elements.

# Set Creation
num_set = {10, 20, 30, 20, 50, 30, 40}
print(num_set)
# Output: {40, 10, 50, 20, 30}

# Creating an empty set (use set(), not {})
empty_group = set()

# Membership Testing
group_a = {5, 10, 15, 20, 10, 5}
print(10 in group_a)  
# Output: True
print(25 in group_a)
# Output: False

# Union (| or union()) - Returns all unique elements
alpha = {1, 2, 7}
beta = {7, 8, 9}
union_res = alpha | beta
print(union_res)
# Output: {1, 2, 7, 8, 9}

# Intersection (& or intersection()) - Common elements
inter_res = alpha & beta
print(inter_res)
# Output: {7}

# Difference (- or difference()) - Elements in alpha not in beta
diff_res = alpha - beta
print(diff_res)
# Output: {1, 2}

# Symmetric Difference (^) - Elements not common
sym_diff = alpha ^ beta
print(sym_diff)
# Output: {1, 2, 8, 9}

# Subset (<= or issubset())
small = {2, 4}
big = {2, 4, 6, 8}
print(small <= big)
# Output: True

# Superset (>= or issuperset())
sup_a = {10, 20, 30}
sup_b = {10, 20}
print(sup_a >= sup_b)
# Output: True

# Disjoint Sets (isdisjoint())
x_set = {3, 6, 9}
y_set = {12, 15, 18}
print(x_set.isdisjoint(y_set))
# Output: True

# Discard, pop, update
random_set = {11, 22, 33, 44, 22}
print(random_set)
# Output: {33, 11, 44, 22}

random_set.discard(99)  # No error even if absent

print(random_set.pop())
# Output (example): 33

print(random_set)
# Output (example): {11, 44, 22}

print(random_set.pop())
# Output (example): 11

random_set.update({55, 66, 11})
print(random_set)
# Output: {66, 22, 44, 55, 11}
