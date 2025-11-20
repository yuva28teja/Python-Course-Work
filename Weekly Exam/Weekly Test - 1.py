# "1: Convert 'Hello World' to lowercase and store in result"
text = "Hello World"
result = text.lower()
print(result)  # Output: "hello world"

# "2: Convert 'good morning' to uppercase this string"
greeting = "good morning"
uppercase_greeting = greeting.upper()
print(uppercase_greeting)  # Output: "GOOD MORNING"

# "3: Remove leading and trailing spaces from ' hello python '"
data = " hello python "
stripped_data = data.strip()
print(stripped_data)  # Output: "hello python"

# "4: Replace 'tough' with 'easy'"
line = "Python is tough"
replaced_line = line.replace("tough", "easy")
print(replaced_line)  # Output: "Python is easy"

# "5: Count 'a' in the word 'banana'"
word = "banana"
count_a = word.count("a")
print(count_a)  # Output: 3

# "6: Split the string into a list of words"
info = "python is fun"
words_list = info.split()
print(words_list)  # Output: ['python', 'is', 'fun']

# "7: Find the length of the string"
sentence = "learn python"
length = len(sentence)
print(length)  # Output: 12

# "8: Check if the string is alphanumeric"
value = "test123"
is_alphanumeric = value.isalnum()
print(is_alphanumeric)  # Output: True

# "9: Convert to lowercase and then capitalize"
text = "HELLO"
lower_then_capitalize = text.lower().capitalize()
print(lower_then_capitalize)  # Output: Hello

# "10: Check if the string ends with '.com'"
email = "student@domain.com"
ends_with_com = email.endswith(".com")
print(ends_with_com)  # Output: True

# "11: Sort the tuple"
marks = (45, 67, 89, 32)
marks_list = sorted(list(marks))
print(marks_list)  # Output: [32, 45, 67, 89]

# "12: Append 40 to the list"
numbers = [10, 20, 30]
numbers.append(40)
print(numbers)  # Output: [10, 20, 30, 40]

# "13: Remove 'blue' from the list"
colors = ["red", "blue", "green"]
colors.remove("blue")
print(colors)  # Output: ['red', 'green']

# "14: Count the occurrences of 2"
values = [1, 2, 3, 2, 1]
count = values.count(2)
print(count)  # Output: 2

# "15: Join the list into a string"
items = ["pen", "book", "pencil"]
joined_string = ", ".join(items)
print(joined_string)  # Output: "pen, book, pencil"

# "16: Reverse the list"
scores = [100, 90, 80]
scores.reverse()
print(scores)  # Output: [80, 90, 100]

# "17: Get the second item from the tuple"
students = ("Anu", "Ravi", "Meena")
second_item = students[1]
print(second_item)  # Output: "Ravi"

# "18: Convert tuple to a list"
details = ("ID101", "Sita", "CSE")
list_details = list(details)
print(list_details)  # Output: ['ID101', 'Sita', 'CSE']

# "19: Find the maximum value in the tuple"
data = (5, 3, 9, 1)
max_value = max(data)
print(max_value)  # Output: 9

# "20: Get the last two elements using slicing"
group = ("A", "B", "C", "D")
last_two = group[-2:]
print(last_two)  # Output: ('C', 'D')

# "21: Convert the list to a set to remove duplicates"
names = ["Anu", "Ravi", "Anu", "Sam"]
unique_names = set(names)
print(unique_names)  # Output: {'Anu', 'Ravi', 'Sam'}

# "22: Find the union of sets a and b"
a = (1, 2, 3)
b = (2, 3, 4)
set_a = set(a)
set_b = set(b)
union = set_a.union(set_b)
print(union)  # Output: {1, 2, 3, 4}

# "23: Find the union of sets x and y"
x = (1, 2, 3)
y = (2, 4)
set_x = set(x)
set_y = set(y)
union = set_x.union(set_y)
print(union)  # Output: {1, 2, 3, 4}

# "24: Add 20 to the set using add()"
numbers = {5, 10, 15}
numbers.add(20)
print(numbers)  # Output: {5, 10, 15, 20}

# "25: Remove 3 from the set using remove()"
items = {1, 2, 3, 4}
items.remove(3)
print(items)  # Output: {1, 2, 4}

# "26: Add a new student 'Sita' with 88 marks to the dictionary"
marks = {"Ravi": 90, "Anu": 85}
marks["Sita"] = 88
print(marks)  # Output: {'Ravi': 90, 'Anu': 85, 'Sita': 88}

# "27: Get the value of 'grade' using get()"
student = {"name": "Asha", "grade": "A"}
grade = student.get("grade")
print(grade)  # Output: A

# "28: Update the value of 'math' to 85"
record = {"math": 75, "science": 80}
record["math"] = 85
print(record)  # Output: {'math': 85, 'science': 80}

# "29: Print all keys of the dictionary using keys()"
profile = {"id": 101, "name": "John"}
print(profile.keys())  # Output: dict_keys(['id', 'name'])

# "30: Remove the key 'y' from the dictionary using pop()"
data = {"x": 1, "y": 2}
data.pop("y")
print(data)  # Output: {'x': 1}