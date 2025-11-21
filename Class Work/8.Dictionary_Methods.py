# A dictionary in Python is an ordered, mutable collection that stores key-value pairs.

# Syntax of a Dictionary:
# dictionary_name = {key1: value1, key2: value2, key3: value3}

# Creating a dictionary:
student = {"name": "Yuva Teja", "Age": 22, "gender": "M"}
print(student)
# Output: {'name': 'Yuva Teja', 'Age': 22, 'gender': 'M'}

# Accessing Values
print(student["name"])      # Yuva Teja
print(student.get("name"))  # -> most preferable

# Adding and updating:
student["college"] = "GRIET"
print(student)
# Output: {'name': 'Yuva Teja', 'Age': 22, 'gender': 'M', 'college': 'GRIET'}

# Removing items:
student.pop("Age")
print(student)

# Removes last item:
student.popitem()
print(student)  # {'name': 'Yuva Teja', 'gender': 'M'}

# Clear:
student.clear()
print(student)  # {}

# Dictionary Built-in Methods
student = {"name": "Yuva Teja", "Age": 22, "gender": "M"}
print(student.keys())       # dict_keys(['name', 'Age', 'gender'])
print(student.values())     # dict_values(['Yuva Teja', 22, 'M'])
print(student.items())      # dict_items([('name', 'Yuva Teja'), ('Age', 22), ('gender', 'M')])

# Dictionary Methods for Adding and Updating Data
student.update({
    "gender": "male",
    "phone": 123456,
    "college": "GRIET"
})
print(student)
# Output: {'name': 'Yuva Teja', 'Age': 22, 'gender': 'male', 'phone': 123456, 'college': 'GRIET'}

student.setdefault("city", "unknown")
print(student['city'])  # unknown

# Dictionary Methods for Removing Data
# pop:
print(student.pop("Age"))

# Using delete:
del student["gender"]
print(student)
# Output: {'name': 'Yuva Teja', 'phone': 123456, 'college': 'GRIET', 'city': 'unknown'}

# Using popitem():
student.popitem()
print(student)
# Output: {'name': 'Yuva Teja', 'phone': 123456, 'college': 'GRIET'}

student.clear()
print(student)  # {}

# Dictionary comprehension:
squares = {x: x*x for x in range(1, 6)}
print(squares)
# Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
