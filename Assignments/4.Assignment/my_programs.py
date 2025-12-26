# my_programs.py
import inspect

# ---------- LOGIC FUNCTIONS ----------

def is_armstrong(n):
    temp = n
    total = 0
    digits = len(str(n))
    while temp > 0:
        total += (temp % 10) ** digits
        temp //= 10
    return total == n


def swap(a, b):
    return b, a


def count_vowels_func(s):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in s:
        if ch in vowels:
            count += 1
    return count


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def reverse_num(n):
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10
        n //= 10
    return rev


def sum_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total


def count_words_func(sentence):
    return len(sentence.split())


def to_title(s):
    return s.title()


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def fibonacci(n):
    a, b = 0, 1
    result = []
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result


def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def is_palindrome(s):
    return s == s[::-1]


def custom_sort_func(lst):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
    return lst


def decimal_to_binary(n):
    return bin(n)[2:]


def even_odd(n):
    return "Even" if n % 2 == 0 else "Odd"


# ---------- DISPLAY FUNCTIONS ----------

def armstrong_number():
    print("Program: Armstrong Number")
    print(inspect.getsource(is_armstrong))
    print("Test Case 1: is_armstrong(153) ->", is_armstrong(153))
    print("Test Case 2: is_armstrong(370) ->", is_armstrong(370))


def swap_numbers():
    print("Program: Swap Two Numbers")
    print(inspect.getsource(swap))
    print("Test Case 1: swap(10, 20) ->", swap(10, 20))
    print("Test Case 2: swap(-5, 3) ->", swap(-5, 3))


def count_vowels():
    print("Program: Count Vowels in String")
    print(inspect.getsource(count_vowels_func))
    print("Test Case 1: count_vowels('hello') ->", count_vowels_func("hello"))
    print("Test Case 2: count_vowels('Python') ->", count_vowels_func("Python"))


def gcd_two_numbers():
    print("Program: GCD of Two Numbers")
    print(inspect.getsource(gcd))
    print("Test Case 1: gcd(12, 18) ->", gcd(12, 18))
    print("Test Case 2: gcd(7, 5) ->", gcd(7, 5))


def reverse_number():
    print("Program: Reverse a Number")
    print(inspect.getsource(reverse_num))
    print("Test Case 1: reverse_num(1234) ->", reverse_num(1234))
    print("Test Case 2: reverse_num(500) ->", reverse_num(500))


def sum_of_digits():
    print("Program: Sum of Digits")
    print(inspect.getsource(sum_digits))
    print("Test Case 1: sum_digits(123) ->", sum_digits(123))
    print("Test Case 2: sum_digits(999) ->", sum_digits(999))


def count_words():
    print("Program: Count Words in Sentence")
    print(inspect.getsource(count_words_func))
    print("Test Case 1:", count_words_func("Hello world"))
    print("Test Case 2:", count_words_func("Python is awesome"))


def title_case():
    print("Program: Convert String to Title Case")
    print(inspect.getsource(to_title))
    print("Test Case 1:", to_title("hello world"))
    print("Test Case 2:", to_title("python programming"))


def prime_check():
    print("Program: Prime Number Check")
    print(inspect.getsource(is_prime))
    print("Test Case 1: is_prime(7) ->", is_prime(7))
    print("Test Case 2: is_prime(10) ->", is_prime(10))


def fibonacci_series():
    print("Program: Fibonacci Series")
    print(inspect.getsource(fibonacci))
    print("Test Case 1:", fibonacci(5))
    print("Test Case 2:", fibonacci(7))


def factorial_number():
    print("Program: Factorial of a Number")
    print(inspect.getsource(factorial))
    print("Test Case 1:", factorial(5))
    print("Test Case 2:", factorial(0))


def palindrome_check():
    print("Program: Palindrome Check")
    print(inspect.getsource(is_palindrome))
    print("Test Case 1:", is_palindrome("madam"))
    print("Test Case 2:", is_palindrome("python"))


def custom_sort():
    print("Program: Custom Sort")
    print(inspect.getsource(custom_sort_func))
    print("Test Case 1:", custom_sort_func([3, 1, 2]))
    print("Test Case 2:", custom_sort_func([5, 4, 1]))


def decimal_to_binary_prog():
    print("Program: Decimal to Binary")
    print(inspect.getsource(decimal_to_binary))
    print("Test Case 1:", decimal_to_binary(10))
    print("Test Case 2:", decimal_to_binary(5))


def even_odd_check():
    print("Program: Even or Odd")
    print(inspect.getsource(even_odd))
    print("Test Case 1:", even_odd(4))
    print("Test Case 2:", even_odd(7))
