# --------------------------------------------
# Q1. Calculate BMI
# --------------------------------------------
def calculate_bmi(weight_kg, height_m):
    bmi = weight_kg / (height_m * height_m)
    return round(bmi, 2)

print(calculate_bmi(70, 1.75))
print(calculate_bmi(90, 1.8))


# --------------------------------------------
# Q2. Filter Even Numbers
# --------------------------------------------
def filter_even(numbers):
    return [i for i in numbers if i % 2 == 0]

print(filter_even([1, 2, 3, 4, 5, 6]))
print(filter_even([11, 15, 21]))


# --------------------------------------------
# Q3. Generate Multiplication Table
# --------------------------------------------
def generate_table(n):
    return [n * i for i in range(1, 11)]

print(generate_table(2))
print(generate_table(5))


# --------------------------------------------
# Q4. Check Anagram
# --------------------------------------------
def is_anagram(str1, str2):
    s1 = sorted(str1.replace(" ", "").lower())
    s2 = sorted(str2.replace(" ", "").lower())
    return s1 == s2

print(is_anagram("listen", "silent"))
print(is_anagram("Hello", "Olelh"))
print(is_anagram("apple", "pale"))


# --------------------------------------------
# Q5. Count Word Occurrences
# --------------------------------------------
def count_words(text):
    words = text.split()
    result = {}
    for w in words:
        result[w] = result.get(w, 0) + 1
    return result

print(count_words("this is a test this is"))
print(count_words("hello hello world"))


# --------------------------------------------
# Q6. Simulate LRU Cache
# --------------------------------------------
def lru_cache(requests, size):
    cache = []
    for item in requests:
        if item in cache:
            cache.remove(item)
            cache.insert(0, item)
        else:
            if len(cache) == size:
                cache.pop()
            cache.insert(0, item)
    return cache

print(lru_cache([1,2,3,2,4,1], 3))
print(lru_cache([5,6,7,8], 2))
print(lru_cache([1,2,3,1], 2))


# --------------------------------------------
# Q7. Flatten 2D List
# --------------------------------------------
def flatten_matrix(matrix):
    result = []
    for row in matrix:
        for val in row:
            result.append(val)
    return result

print(flatten_matrix([[1, 2], [3, 4]]))
print(flatten_matrix([[5], [6, 7], [8]]))


# --------------------------------------------
# Q8. Create Email Address
# --------------------------------------------
def create_email(first_name, last_name, domain):
    return f"{first_name.lower()}.{last_name.lower()}@{domain.lower()}.com"

print(create_email("John", "Doe", "gmail"))
print(create_email("ALICE", "Smith", "yahoo"))


# --------------------------------------------
# Q9. Find All Factors of a Number
# --------------------------------------------
def get_factors(n):
    factors = []
    for i in range(1, n//2 + 1):
        if n % i == 0:
            factors.append(i)
    factors.append(n)
    return factors

print(get_factors(12))
print(get_factors(17))
print(get_factors(28))


# --------------------------------------------
# Q10. Format Invoice Entry
# --------------------------------------------
def format_invoice(item, quantity, price):
    total = quantity * price
    return f"{item} x{quantity} @ ₹{price} = ₹{total}"

print(format_invoice("Pen", 3, 10))
print(format_invoice("Notebook", 2, 45))
