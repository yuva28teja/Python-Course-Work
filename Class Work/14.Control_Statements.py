# ---------------- CONTROL STATEMENTS ----------------
# break → stops the loop immediately
# continue → skips the current iteration and continues
# pass → does nothing (placeholder)

# ---------------- FOR LOOP DEFINITION ----------------
# for loop is used when the number of iterations is known.

# ---------------- WHILE LOOP DEFINITION ----------------
# while loop runs as long as the condition is TRUE.


# -------------------------------------------------------
#                     SET (FOR LOOP)
# -------------------------------------------------------
lang = {'python','java','c','c++','mysql','ds','flask','javascript'}

print("FOR LOOP → Iterating over set:")
for i in lang:
    print(i)

print("\nWHILE LOOP → Iterating over set:")
lang_list = list(lang)
i = 0
while i < len(lang_list):
    print(lang_list[i])
    i += 1


# -------------------------------------------------------
#                     ENUMERATE (SET)
# -------------------------------------------------------
print("\nFOR → Enumerate set:")
for item in enumerate(lang):
    print(item)

print("\nWHILE → Enumerate set:")
i = 0
while i < len(lang_list):
    print((i, lang_list[i]))
    i += 1


# -------------------------------------------------------
#                     DICTIONARY
# -------------------------------------------------------
l = {1:'python', 2:'java', 3:'c', 4:'c++'}

print("\nFOR → Iterating dictionary:")
for key in l:
    print(f'key-{key} value-{l[key]}')

print("\nWHILE → Iterating dictionary:")
keys = list(l.keys())
i = 0
while i < len(keys):
    print(f'key-{keys[i]} value-{l[keys[i]]}')
    i += 1


# -------------------------------------------------------
#                     STRING
# -------------------------------------------------------
string = "python"

print("\nFOR → Iterating string:")
for ch in string:
    print(ch)

print("\nWHILE → Iterating string:")
i = 0
while i < len(string):
    print(string[i])
    i += 1


# -------------------------------------------------------
#                     RANGE
# -------------------------------------------------------
print("\nFOR → Even numbers 2 to 10:")
for i in range(2, 11, 2):
    print(i)

print("\nWHILE → Even numbers 2 to 10:")
i = 2
while i <= 10:
    print(i)
    i += 2


# -------------------------------------------------------
#             Multiplication Table
# -------------------------------------------------------
num = 5

print(f"\nFOR → Table of {num}:")
for i in range(1, 11):
    print(f"{num} * {i} = {num*i}")

print(f"\nWHILE → Table of {num}:")
i = 1
while i <= 10:
    print(f"{num} * {i} = {num*i}")
    i += 1


# -------------------------------------------------------
#             LIST & TUPLE ITERATION
# -------------------------------------------------------
list_a = ['laptop','mouse','charger','keyboard']

print("\nFOR → List items:")
for i in range(len(list_a)):
    print(i, list_a[i])

print("\nWHILE → List items:")
i = 0
while i < len(list_a):
    print(i, list_a[i])
    i += 1


tuple_a = ('laptop','mouse','charger','keyboard')

print("\nFOR → Tuple items:")
for i in range(len(tuple_a)):
    print(i, tuple_a[i])

print("\nWHILE → Tuple items:")
i = 0
while i < len(tuple_a):
    print(i, tuple_a[i])
    i += 1


# -------------------------------------------------------
#                     CONTINUE
# -------------------------------------------------------
print("\nFOR → continue example:")
for i in range(5):
    if i == 2:
        continue
    print(i)

print("\nWHILE → continue example:")
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)


# -------------------------------------------------------
#                     BREAK
# -------------------------------------------------------
print("\nFOR → break example:")
for i in range(5):
    if i == 2:
        break
    print(i)

print("\nWHILE → break example:")
i = 0
while i < 5:
    if i == 2:
        break
    print(i)
    i += 1
