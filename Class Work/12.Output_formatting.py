# basic printing a text:
print("hello.World!")  # hello.World!

# printing multiple items:
name = "Yuvateja"
batch = "PFS-041"
print("name: ", name, "batch: ", batch)
# Output: name:  Yuvateja batch:  PFS-041

# using sep:
print("2025", "07", "10", sep="-")
# Output: 2025-07-10

# using end:
print("hello", "python", end=" ")
# Output: hello python 

# new line:
print("line1\nline2")  

# Output:
# line1
# line2

# \tab: it provides 4 spaces:
print("hello\t,world")
# Output: hello    ,world

# output formatting methods:
name = "Yuvateja"
age = 22
cgpa = 7.45

# 1. comma-separated:
print("name: ", name, "Age: ", age, "cgpa: ", cgpa)
# Output: name:  Yuvateja Age:  22 cgpa:  7.45

# 2. using modulo operator:
print("name:%s | Age:%d | cgpa:%f" % (name, age, cgpa))
# Output: name:Yuvateja | Age:22 | cgpa: 7.450000

# 3. f-strings:
print(f"name:{name} age:{age} cgpa:{cgpa}")
# Output: name:Yuvateja age:22 cgpa:7.45

# 4. str.format() method:
print("Name: {} Age: {} cgpa: {}".format(name, age, cgpa))
# Output: Name: Yuvateja Age: 22 cgpa: 7.45
