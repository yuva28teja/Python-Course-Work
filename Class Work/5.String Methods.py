# ================================================================
# Alignment & Formatting Methods
# ================================================================
print("Alignment & Formatting Methods")

s = "python"

print(s.center(12, "*"))          # Output: ***python***
print(s.ljust(12, "-"))           # Output: python------
print(s.rjust(12, "+"))           # Output: ++++++python
print("543".zfill(8))             # Output: 00000543

print()


# ================================================================
# Search & Find Methods
# ================================================================
print("Search & Find Methods")

s = "hello python programming"

print(s.find("python"))           # Output: 6
print(s.rfind("o"))               # Output: 22
print(s.index("programming"))     # Output: 13
print(s.count("o"))               # Output: 3

print()


# ================================================================
# Replace & Modify Methods
# ================================================================
print("Replace & Modify Methods")

s = "apple apple mango apple"

print(s.replace("apple", "banana"))
# Output: banana banana mango banana

# translate() + maketrans()
table = str.maketrans("aeiou", "12345")
print("hello world".translate(table))
# Output: h2ll4 w4rld

print()


# ================================================================
# Splitting & Joining Methods
# ================================================================
print("Splitting & Joining Methods")

s = 'python programming lang'
print(s.split())  
# Output: ['python', 'programming', 'lang']

s = 'python,java,sql,flask,html,css'
print(s.split(','))  
# Output: ['python', 'java', 'sql', 'flask', 'html', 'css']

print(s.rsplit(','))  
# Output: ['python', 'java', 'sql', 'flask', 'html', 'css']

print(s.rsplit(',', 3))  
# Output: ['python,java,sql', 'flask', 'html', 'css']

s2 = """python
java
sql
flask
html
css"""

print(s2.splitlines())  
# Output: ['python', 'java', 'sql', 'flask', 'html', 'css']

# join() examples
s3 = "pythonjavasqlflaskhtmlcss"
print(",".join(s3))  
# Output: p,y,t,h,o,n,j,a,v,a,s,q,l,f,l,a,s,k,h,t,m,l,c,s,s

print("".join(s3))  
# Output: pythonjavasqlflaskhtmlcss

# partition
s = 'python,java,sql,flask,html,css'
print(s.partition(','))  
# Output: ('python', ',', 'java,sql,flask,html,css')

print(s.rpartition(','))  
# Output: ('python,java,sql,flask,html', ',', 'css')

print()


# ================================================================
# Whitespace & Trimming Methods
# ================================================================
print("Whitespace & trimming Methods")

s = '     python'

print(s.strip())                 # Output: python
print(s.lstrip())                # Output: python
print(s.rstrip())                # Output: '     python'

print()


# ================================================================
# Encode & Decode Methods
# ================================================================
print("Encode & Decode Methods")

s = 'hello'
print(s.encode())                # Output: b'hello'

print()


# ================================================================
# String Testing Methods
# ================================================================
print("String Testing Methods")

s = 'python.py'
print(s.startswith('pyt'))       # Output: True
print(s.endswith('.py'))         # Output: True

s = 'YUVATEJA'
print(s.isalpha())               # Output: True

s = 'yuvateja125'
print(s.isalnum())               # Output: True

s = 'yuvateja'
print(s.islower())               # Output: True

s = 'YUVATEJA'
print(s.isupper())               # Output: True

s = 'yuva teja'
print(s.isspace())               # Output: False
print(s.istitle())               # Output: False
print(s.isidentifier())          # Output: False

print(len(s))                    # Output: 9
print(max(s))                    # Output: 'v'
print(min(s))                    # Output: ' '

print(sorted(s))                 
# Output: [' ', 'a', 'a', 'e', 'j', 't', 'u', 'v', 'y']

print(ord(s[0]))                 # Output: 121
print(chr(121))                  # Output: y

print()


# ================================================================
# Operations on Strings
# ================================================================
print("Concatenation")

a = "yuva"
b = "teja"
print(a + b)                     # Output: yuvateja

d = a + b
print()

print("Repetition")
print(a * 5)                     # Output: yuvayuvayuvayuvayuva
print()

print("Indexing")
print(d[0])                      # Output: y
print(d[-1])                     # Output: a
print()

print("Slicing")
print(d[0:8])                    # Output: yuvateja
print(d[0:])                     # Output: yuvateja
print(d[4:])                     # Output: teja
print(d[::2])                    # Output: yvae
print()

print(d[::-1])                   # Output: ajetavuy
print(d[7:3:-1])                 # Output: ajet
print(d[3::-1])                  # Output: avuy
print()


# ================================================================
# Membership
# ================================================================
print("Membership")

print("yuva in a:", "yuva" in a)            # Output: True
print("teja not in b:", "teja" not in b)    # Output: False

print()


# ================================================================
# Case Conversion Methods
# ================================================================
print("Case Conversion Methods")

print("upper()", d.upper())               # Output: YUVATEJA
print("lower()", d.lower())               # Output: yuvateja
print("capitalize()", d.capitalize())     # Output: Yuvateja
print("title()", d.title())               # Output: Yuvateja
print("swapcase()", d.swapcase())         # Output: yUVATEJA
print("casefold()", d.casefold())         # Output: yuvateja
print()
