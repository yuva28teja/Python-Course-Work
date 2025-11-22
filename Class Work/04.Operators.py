'''Python Operators
--------------'''

# 1. Arithmetic operators
a = 10
b = 20
print("a+b:", a + b)          # Output: 30
print("a-b:", a - b)          # Output: -10
print("a*b:", a * b)          # Output: 200
print("a/b:", a / b)          # Output: 0.5
print("a//b:", a // b)        # Output: 0
print("a**b:", a ** b)        # Output: 100000000000000000000
print("________________________________________")
# 2. Comparison Operators
c = 30
d = 40
print("c<d:", c < d)          # Output: True
print("c>d:", c > d)          # Output: False
print("c<=d:", c <= d)        # Output: True
print("c>=d:", c >= d)        # Output: False
print("c==d:", c == d)        # Output: False
print("c!=d:", c != d)        # Output: True
print("________________________________________")

# 3. Assignment Operators
e = 100
e += 100
print('e += 100:', e)         # Output: 200
e -= 100
print('e -= 100:', e)         # Output: 100
e *= 100
print('e *= 100:', e)         # Output: 10000
e //= 100
print('e //= 100:', e)        # Output: 100
e **= 10
print('e **= 10:', e)         # Output: 10000000000000000000000000000000000000000
e %= 3
print('e %= 3:', e)           # Output: 1
e /= 5
print('e /= 5:', e)           # Output: 0.2
print("________________________________________")

# 4. Logical Operators
x = 100
y = 50
print("x%20==0 and y%20==0:", x % 20 == 0 and y % 20 == 0)   # Output: True
print("x%20==0 or y%20==0:", x % 20 == 0 or y % 20 == 0)     # Output: True
print("not x%20==0:", not x % 20 == 0)                       # Output: False
print("not y%20==0:", not y % 20 == 0)                       # Output: False
print("________________________________________")

# 5. Membership Operators
s = 'Python Programming'
print("i in s:", "i" in s)                      # Output: True
print("x not in s:", "x" not in s)              # Output: True

l = [1, 2, 3, 4, 5]
print("3 in l:", 3 in l)                        # Output: True
print("10 not in l:", 10 not in l)              # Output: True

t = (102, 103, 104, 105)
print("108 in t:", 108 in t)                    # Output: False

se = {10, 20, 30, 40}
print("40 in se:", 40 in se)                    # Output: True
print("50 not in se:", 50 not in se)            # Output: True

d = {1: 1, 2: 4, 3: 9, 4: 16}
print("1 in d (checks keys only):", 1 in d)     # Output: True
print("4 in d (checks keys only):", 4 in d)     # Output: True
print("________________________________________")

# 6. Identity Operators
f = [1, 2, 3, 4]
g = [1, 2, 3, 4]
print("f == g:", f == g)                        # Output: True
print("f is g:", f is g)                        # Output: False

h = f
print("f == h:", f == h)                        # Output: True
print("f is h:", f is h)                        # Output: True

print("id(f):", id(f))                          # Example Output: 140532479103232
print("id(g):", id(g))                          # Example Output: 140532479103680
print("id(h):", id(h))                          # Same as id(f)

print("f is not g:", f is not g)                # Output: True
print("f is not h:", f is not h)                # Output: False
print("________________________________________")

# 7. Bitwise Operators
"""
1-0001
2-0010
3-0011
4-0100
5-0101
6-0110
7-0111
8-1000
9-1001
10-1010
11-1011
12-1100
13-1101
14-1110
15-1111

&-Gate
00-0
01-0
10-0
11-1

4-0100
5-0101
------
  0100
------

|-Gate
00-0
01-1
10-1
11-1

11-1011
12-1100
--------
   1111
--------

^ -Gate (XOR), same bits 0,diff bits 1
00-0
01-1
10-1
11-0

14-1110
15-1111
-------
   0001
-------

~Gate (not gate)
0-1
1-0

left shift<< (zeros added to right) value increse

right shift>> (zeros added to left) value decrese
"""

print('4 & 5:', 4 & 5)                           # Output: 4
print('11 | 12:', 11 | 12)                       # Output: 15
print('14 ^ 15:', 14 ^ 15)                       # Output: 1
print("~16:", ~16)                                # Output: -17
print("8 << 1:", 8 << 1)                          # Output: 16
print("16 >> 1:", 16 >> 1)                        # Output: 8
