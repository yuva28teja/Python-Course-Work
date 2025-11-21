# 1. Converting from int
int_a = 5
print(float(int_a))  # 5.0
print(str(int_a))    # '5'
print(bool(int_a))   # True


# Converting from float
float_b = 5.78
print(int(float_b))  # 5
print(str(float_b))  # '5.78'
print(bool(float_b)) # True


# Converting from string
str_c = '12'
print(int(str_c))    # 12
print(list(str_c))   # ['1', '2']
print(tuple(str_c))  # ('1', '2')
print(set(str_c))    # {'1', '2'}


# Converting from tuple
tup_d = (1, 2, 3, 4)
print(str(tup_d))    # '(1, 2, 3, 4)'
print(list(tup_d))   # [1, 2, 3, 4]
print(set(tup_d))    # {1, 2, 3, 4}


# Converting from set
set_e = {3, 4, 5, 6, 7}
print(str(set_e))    # '{3, 4, 5, 6, 7}'
print(list(set_e))   # [3, 4, 5, 6, 7]
print(tuple(set_e))  # (3, 4, 5, 6, 7)


# Converting from dictionary
dict_d = {1: "dinesh", 2: "Deepak", 3: "Raju"}
print(list(dict_d))  # [1, 2, 3]


# Dictionary conversion (UPDATED → name: 'yuvateja')
d = [('name', 'yuvateja'), ('batch', '22'), ('subject', 'python')]
print(dict(d))  # {'name': 'yuvateja', 'batch': '22', 'subject': 'python'}
