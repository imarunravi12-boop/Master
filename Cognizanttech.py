from collections import Counter

# 1.In simple terms, a palindrome is a word, phrase, number, or sequence that reads the same backward as forward
def is_palindrome(text):
    return text == text [::-1]

word = ["madam","hello","python"]
for item in word:
    if is_palindrome(item):
        print(f"{item} :is a palindrome")
    else:
        print(f"{item} :is not a palindrome")

# 2. In mathematics and programming, a Factorial is the product of all positive integers less than or equal to a given number $n$. It is written as $n!$
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))

# 3. The Fibonacci sequence is a famous series of numbers where each number is the sum of the two preceding ones. It usually starts with 0 and 1.
def fibonacci(n):
    a, b = 0,1
    for item in range(n):
        print(a, end = " ")
        a,b = b, a + b
print(fibonacci(10))

# 4. Print duplicate numbers in a list
numbers = [1,2,3,4,5,6,7,8,1,2,3,4]
duplicate = []
for item in numbers:
    if item not in duplicate:
        duplicate.append(item)
    else:
        print(f"Duplicate number:",item)

#5. Remove vowels from a string
word = "python automation testing"
vowels = 'aeiou'
remove = []
for item in word:
    if item not in vowels:
        remove.append(item)

result = ''.join(remove)
print(result)

# 6.Prime number is a natural number greater than 1 that cannot be formed by multiplying two smaller natural numbers. A prime number is only divisible by 1 and itself.
num = 24
if num <= 1:
    print("Not a prime number")
else:
    for item in range(2,num):
        if num % item == 0:
            print("Not a prime number")
            break
    else:
        print("Is a prime number")

# 7.Remove speak characters
word = "Python@#Automation!@##Testing$%^&*()"
words = ""
for item in word:
    if item.isalnum():
        words = words + item
result = "".join(words)
print(result)

# 8.Ascending in a list
number = [5,6,1,4,2,3]
for i in range(len(number)):
    for j in range(i+1,len(number)):
        if number[i] > number[j]:
            number[i],number[j]=number[j],number[i]
print(number)

# descending in a list
number = [5,6,1,4,2,3]
for i in range(len(number)):
    for j in range(i+1,len(number)):
        if number[i] < number[j]:
            number[i],number[j]=number[j],number[i]
print(number)

# 9.Find the largest word in a list
words = ["python","automation","testing","cognizant"]
largest = []
for item in words:
    if len(item) > len(largest):
        largest = item
print(largest)

# 10. Count the uppercase letters
word = "Python Automation Testing"
count = 0
for item in word:
    if item.isupper():
        count = count + 1
print(f"Uppercase Count:",count)

# 11. two dictionaries and add the values for keys that exist in both
dict1 = {"apple":5,"orange":10}
dict2 = {"apple":10,"mango":20}
word = Counter(dict1) + Counter(dict2)
print(dict(word))

# 12. Count the frequency of characters in a string.
word = "aabbccddeeff"
words = {}
for item in word:
    if item in words:
        words[item] +=1
    else:
        words[item] = 1
print(words)

# 13. Find the common elements between three lists.
list1 = [1,2,3,4,5,6]
list2 = [1,2,3,4,5,6,7,8]
list3 = [1,2,3,4,4,5,6,7,8,9,10]

common_element = []
for item in list1:
    if item in list2 and item in list3:
        common_element.append(item)
print(common_element)

# 15. Find pairs of numbers in a list that add up to a specific target.
numbers = [2,7,11,15]
target = 9
for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        if numbers[i] + numbers[j] == target:
            print(f"pair found: {numbers[i],numbers[j]}")

#16 .Merge two lists into a single list of strings, where each string is a combination of the corresponding elements from both lists.
list = ["a","b","c","d","e","f"]
number = [1,1,1,1]
output = []
for item in list:
    if number:
        output.append(f"{item}{number.pop(0)}")
    else:
        output.append(item)
print(output)

#17. Find the non-repeating characters in a string.
word = "racecar"
counts = {}
for item in word:
    if item in counts:
        counts[item] += 1
    else:
        counts[item] = 1

non_repeating = []
for item in word:
    if counts[item] == 1:
        non_repeating.append(item)
print(non_repeating)

# 18. Find the duplicate elements in a list.
list1 = ["admin","admin"]
list2 = ["admin","admin@123"]

duplicate = []
original= []
for item in list2:
    if item in list1:
        if item not in duplicate:
            duplicate.append(item)
    else:
        original.append(item)
print(duplicate)
print(original)


# 19. Remove duplicate characters from a string while preserving the order of characters.
word = "abccabcba"
words = []
for item in word:
    if item not in words:
        words.append(item)
texts = len(words)
text = "".join(words)
print(text)
print(texts)

# 20 . Given a list of integers, create a new list that contains the squares of the positive numbers and the cubes of the negative numbers, while ignoring zeros.
# data = [1, 4, -2, 10, 7, -5, 8]
# Expected Output: [1, 40, 100, 7, 80]

data = [1, 4, -2, 10, 7, -5, 8]
output = []

for item in data:
    if item > 0:
        if item % 2 ==0:
            output.append(item*10)
        else:
            output.append(item)
print(output)

# 21. Count the frequency of each character in a string and print the characters that appear more than once along with their counts.
# word = "testautomation"
# Expected Output: {'t': 4, 'a': 2, 'o': 2}
# (Because 'e', 's', 'u', 'm', 'i', 'n' only appear once)

word = "testautomation"
count = {}
for item in word:
    if item in count:
        count[item] += 1
    else:
        count[item] = 1
result = {}
for key, value in count.items():
    if value > 1:
        result[key] = value
print(result)


# 22. Square them: [4, 25, 64, 81, 64, 100, 9]
# Filter > 50: [64, 81, 64, 100]
# Remove duplicates: [64, 81, 100]
# Expected Output: [64, 81, 100] (order doesn't matter)

number = [4, 25, 64, 81, 64, 100, 9]
numbers = []
for item in number:
    if item > 50:
        if item not in numbers:
            numbers.append(item)
print(numbers)

# 23. The "Expensive" Products
products = {
    "Laptop": 1200,
    "Mouse": 25,
    "Monitor": 300,
    "Keyboard": 50,
    "Smartphone": 800
}
Expected_Output = []
for name,price in products.items():
    if price > 500:
        Expected_Output.append(name)
print(Expected_Output)

# 24. Combine the nested lists into a single flat list.
# nested_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
# Expected Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

nested_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
combine_list = []
for item in nested_list:
    for items in item:
        combine_list.append(items)
print(combine_list)

# 25. Count the number of vowels in a string and create a dictionary with the vowel as the key and its count as the value.
# word = "automation"
# Expected Output: {'a': 2, 'u': 1, 'o': 2, 'i': 1}

word = "automation"
vowels = "aeiou"
count = {}
for item in word:
    if item in vowels:
        if item in count:
            count[item] +=1
        else:
            count[item] =1
print(count)

# 26. Invert a dictionary, swapping keys and values.
# data = {"Arun": 101, "Alice": 102, "Bob": 103}
# Expected Output: {101: 'Arun', 102: 'Alice', 103: 'Bob'}
data = {"Arun": 101, "Alice": 102, "Bob": 103}
reversed_data = {}
for name,number in data.items():
    reversed_data[number] = name
print(reversed_data)

# 27. Given a dictionary of student names and their scores, create a new dictionary that categorizes students as "Pass" or "Fail" based on a passing score of 60.
# Expected Output: {'Arun': 'Pass', 'Bob': 'Pass'}
scores = {
    "Arun": 85,
    "Alice": 62,
    "Bob": 90,
    "Charlie": 45
}

Expected_Output = {}
for name,value in scores.items():
    if value >= 70:
        Expected_Output[name] = "Pass"
print(Expected_Output)

# 28. Find the most expensive product in a list of dictionaries.ven a list of products with their prices, find the most expensive product and print its name.
products = [
    {"name": "Laptop", "price": 1200},
    {"name": "Mouse", "price": 25},
    {"name": "Monitor", "price": 300},
    {"name": "Smartphone", "price": 800}
]

max_price = 0
expensive_product = ""
for item in products:
    if item["price"] > max_price:
        max_price = item["price"]
        expensive_product = item["name"]
print(expensive_product)


