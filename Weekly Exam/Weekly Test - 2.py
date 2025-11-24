# ----------------------------------------------------
# 1. Birthday Format Fixer
# ----------------------------------------------------
date, month, year = input().split("-")
print(f"{year}/{month}/{date}")

# Input: 12-09-2002
# Output: 2002/09/12


# ----------------------------------------------------
# 2. Even Odd Game
# ----------------------------------------------------
number = int(input())
if number % 2 == 0:
    print("Even Winner")
else:
    print("Odd number")

# Input: 45
# Output: Odd number


# ----------------------------------------------------
# 3. Vowel Replacer Bot
# ----------------------------------------------------
String = input().lower()
print(String.translate(str.maketrans("aeiou", "*****")))

# Input: programming hero
# Output: pr*gr*mm*ng h*r*


# ----------------------------------------------------
# 4. Shopping Cart Analyzer
# ----------------------------------------------------
prices = list(map(float, input().split(",")))
print(f"maxprices:{max(prices)}")
print(f"total price:{sum(prices)}")

# Input: 10, 50.5, 6.75, 99, 2
# Output:
# maxprices:99.0
# total price:168.25


# ----------------------------------------------------
# 5. Secure Login System
# ----------------------------------------------------
credentials = ("admin", "python123")
username = input()
password = input()
if (username,password) == credentials:
    print("Login Succesful")
else:
    print("Access Denied")

# Input:
# admin
# python123
# Output: Login Succesful

# Another Input:
# guest
# guest123
# Output: Access Denied


# ----------------------------------------------------
# 6. Remove Duplicates from Set
# ----------------------------------------------------
names = set(input().split(","))
names = list(names)
print(names)

# Input: apple,banana,apple,grape,banana,mango
# Output: ['banana', 'apple', 'mango', 'grape']
# (Order may vary)


# ----------------------------------------------------
# 7. Student Marks Record
# ----------------------------------------------------
max_marks = 0
res = ""
students = int(input("Enter number of students: "))
students_list = {}

for i in range(students):
    name, marks = input("Enter name and marks (comma-separated): ").split(",")
    marks = int(marks)
    students_list[name] = marks
    if marks > max_marks:
        max_marks = marks
        res = name

print(res)

# Input:
# Enter number of students: 3
# Enter name and marks (comma-separated): Teja,88
# Enter name and marks (comma-separated): Rohit,92
# Enter name and marks (comma-separated): Kiran,85
# Output: Rohit


# ----------------------------------------------------
# 8. Reversing My String
# ----------------------------------------------------
sentence = input().split()
for i in sentence:
    print(i[::-1], end=" ")

# Input: python coding
# Output: nohtyp gnidoc


# ----------------------------------------------------
# 9. Clean My List
# ----------------------------------------------------
numbers = list(map(int, input().split()))
new_list = []
for i in range(len(numbers)):
    if numbers[i] != 0:
        new_list.append(numbers[i])
print(new_list)

# Input: 0 7 0 9 10 0 5
# Output: [7, 9, 10, 5]


# ----------------------------------------------------
# 10. Frequency Counter
# ----------------------------------------------------
statement = input("Enter a string: ").replace(" ", "")
frequency = {}

for char in statement:
    if char not in frequency:
        frequency[char] = 1
    else:
        frequency[char] += 1

print(frequency)

# Input: banana
# Output: {'b': 1, 'a': 3, 'n': 2}
