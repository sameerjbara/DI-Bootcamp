# Exercise 1
# Instructions
# Write a script that inserts an item at a defined index in a list.

lst = [1, 2, 4, 5]
lst.insert(2, 3)
print(lst)


# Exercise 2
# Instructions
# Write a script that counts the number of spaces in a string.

text = "Hello world this is Python"
count = 0

for ch in text:
    if ch == " ":
        count += 1

print(count)


# Exercise 3
# Instructions
# Write a script that calculates the number of upper case letters and lower case letters in a string.

text = "Hello World"
upper = 0
lower = 0

for ch in text:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1

print("Uppercase:", upper)
print("Lowercase:", lower)


# Exercise 4
# Instructions
# Write a function to find the sum of an array without using the built in function:

# >>>my_sum([1,5,4,2])
# >>>12

def my_sum(lst):
    total = 0
    for n in lst:
        total += n
    return total

print(my_sum([1, 5, 4, 2]))


# Exercise 5
# Instructions
# Write a function to find the max number in a list

# >>>find_max([0,1,3,50])
# >>>50

def find_max(lst):
    max_val = lst[0]
    for n in lst:
        if n > max_val:
            max_val = n
    return max_val

print(find_max([0, 1, 3, 50]))


# Exercise 6
# Instructions
# Write a function that returns factorial of a number

# >>>factorial(4)
# >>>24

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial(4))


# Exercise 7
# Instructions
# Write a function that counts an element in a list (without using the count method):

# >>>list_count(['a','a','t','o'],'a')
# >>>2

def list_count(lst, value):
    count = 0
    for item in lst:
        if item == value:
            count += 1
    return count

print(list_count(['a', 'a', 't', 'o'], 'a'))


# Exercise 8
# Instructions
# Write a function that returns the L2-norm (square root of the sum of squares) of the sum of a list:

# >>>norm([1,2,2])
# >>>3

import math

def norm(lst):
    total = 0
    for n in lst:
        total += n ** 2
    return math.sqrt(total)

print(norm([1, 2, 2]))


# Exercise 9
# Instructions
# Write a function to find if an array is monotonic (sorted either ascending of descending)

# >>>is_mono([7,6,5,5,2,0])
# >>>True

# >>>is_mono([2,3,3,3])
# >>>True

# >>>is_mono([1,2,0,4])
# >>>False

def is_mono(lst):
    inc = True
    dec = True

    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            inc = False
        if lst[i] < lst[i + 1]:
            dec = False

    return inc or dec

print(is_mono([7, 6, 5, 5, 2, 0]))
print(is_mono([2, 3, 3, 3]))
print(is_mono([1, 2, 0, 4]))


# Exercise 10
# Instructions
# Write a function that prints the longest word in a list.

def longest_word(words):
    longest = words[0]
    for w in words:
        if len(w) > len(longest):
            longest = w
    print(longest)

longest_word(["hello", "world", "python", "programming"])


# Exercise 11
# Instructions
# Given a list of integers and strings, put all the integers in one list, and all the strings in another one.

def separate_types(lst):
    nums = []
    strs = []

    for item in lst:
        if isinstance(item, int):
            nums.append(item)
        elif isinstance(item, str):
            strs.append(item)

    return nums, strs

print(separate_types([1, "a", 2, "b", 3]))


# Exercise 12
# Instructions
# Write a function to check if a string is a palindrome:

# >>>is_palindrome('radar')
# >>>True

# >>>is_palindrome('John)
# >>>False

def is_palindrome(text):
    return text == text[::-1]

print(is_palindrome("radar"))
print(is_palindrome("John"))


# Exercise 13
# Instructions
# Write a function that returns the amount of words in a sentence with length > k:

# >>>sentence = 'Do or do not there is no try'
# >>>k=2
# >>>sum_over_k(sentence,k)
# >>>3
def sum_over_k(sentence, k):
    count = 0
    for word in sentence.split():
        if len(word) > k:
            count += 1
    return count

sentence = "Do or do not there is no try"
print(sum_over_k(sentence, 2))


# Exercise 14
# Instructions
# Write a function that returns the average value in a dictionary (assume the values are numeric):

# >>>dict_avg({'a': 1,'b':2,'c':8,'d': 1})
# >>>3

def dict_avg(d):
    total = 0
    count = 0

    for value in d.values():
        total += value
        count += 1

    return total / count

print(dict_avg({'a': 1, 'b': 2, 'c': 8, 'd': 1}))

# Exercise 15
# Instructions
# Write a function that returns common divisors of 2 numbers:

# >>>common_div(10,20)
# >>>[2,5,10]

def common_div(a, b):
    result = []
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            result.append(i)
    return result

print(common_div(10, 20))

# Exercise 16
# Instructions
# Write a function that test if a number is prime:

# >>>is_prime(11)
# >>>True

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print(is_prime(11))


# Exercise 17
# Instructions
# Write a function that prints elements of a list if the index and the value are even:

# >>>weird_print([1,2,2,3,4,5])
# >>>[2,4]

def weird_print(lst):
    result = []
    for i in range(len(lst)):
        if i % 2 == 0 and lst[i] % 2 == 0:
            result.append(lst[i])
    return result

print(weird_print([1, 2, 2, 3, 4, 5]))


# Exercise 18
# Instructions
# Write a function that accepts an undefined number of keyworded arguments and return the count of different types:

# >>>type_count(a=1,b='string',c=1.0,d=True,e=False)
# >>>int: 1, str:1 , float:1, bool:2

def type_count(**kwargs):
    types = {}

    for value in kwargs.values():
        t = type(value).__name__
        types[t] = types.get(t, 0) + 1

    for k, v in types.items():
        print(f"{k}: {v}", end=", ")

type_count(a=1, b="string", c=1.0, d=True, e=False)


# Exercise 19
# Instructions
# Write a function that mimics the builtin .split() method for strings.

# By default the function uses whitespace but it should be able to take an argument for any character and split with that argument.

def my_split(text, sep=" "):
    result = []
    word = ""

    for ch in text:
        if ch == sep:
            result.append(word)
            word = ""
        else:
            word += ch

    result.append(word)
    return result

print(my_split("hello world"))
print(my_split("a,b,c", ","))


# Exercise 20
# Instructions
# Convert a string into password format.

# Example:
# input : "mypassword"
# output: "***********"

def password_mask(text):
    return "*" * len(text)

print(password_mask("mypassword"))
