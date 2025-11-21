# 1. String Input
name = input("Enter your full name: ")
print("Name:", name)
# Example Input: Yuvateja
# Output: Name: Yuvateja


# 2. Integer Input
quantity = int(input("Enter the number of items: "))
print("Quantity:", quantity)
# Example Input: 5
# Output: Quantity: 5


# 3. Float Input
discount = float(input("Enter the discount: "))
print("Discount:", discount)
# Example Input: 10.5
# Output: Discount: 10.5


# 4. Input as List (space-separated)
tags = input("Enter tags (space separated): ").split()
print("Tags (space separated):", tags)
# Example Input: python java ai
# Output: ['python', 'java', 'ai']


# 5. Input as List (comma-separated)
tags2 = input("Enter tags (comma separated): ").split(',')
print("Tags (comma separated):", tags2)
# Example Input: red,blue,green
# Output: ['red', 'blue', 'green']


# 6. Input list of integers
marks = list(map(int, input("Enter list of numbers: ").split()))
print("Marks list:", marks)
# Example Input: 10 20 30 40
# Output: [10, 20, 30, 40]


# 7. Input set of integers
marks2 = set(map(int, input("Enter your marks: ").split()))
print("Marks set:", marks2)
# Example Input: 90 85 76
# Output: {90, 76, 85}


# 8. Eval input (dictionary/list/tuple)
profile = eval(input("Enter profile (dict/list/tuple): "))
print("Profile:", profile)
# Example Input: {"id": 1, "name": "Yuva"}
# Output: {'id': 1, 'name': 'Yuva'}


# 9. Multiple Inputs with Unpacking
username, password = input("Enter username and password: ").split()
print("Username:", username)
print("Password:", password)
# Example Input: yuva 1234
# Output:
# Username: yuva
# Password: 1234
