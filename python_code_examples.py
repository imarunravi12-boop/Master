#revserse slicing method in python
reverse = "Hello world"
reverse_text = reverse[::-1]
print(reverse_text)

# reverse method
reverse = "Arun kumar"
reverse_text =""
for char in reverse:
    reverse_text = char + reverse_text
print(reverse_text)

# reverse word in string
reverse = "welcome to wipro"
words = reverse.split()
words = words[::-1]
words[2] = words[2] [::-1]
result = " ".join(words)
print(result)

# duplicate in python string
duplicates = "aaaabbbccccccdddddeee"
duplicate_string = []
for item in duplicates:
    if item not in duplicate_string:
        duplicate_string.append(item)
print(duplicate_string)

# reverse word using for loop
word = "python automation"
words = word.split()
frist_word = words[0]
reverse = ""
for item in range(len(frist_word)-1,-1,-1):
    reverse += frist_word[item]

words[0] = reverse
text = " ".join(words)
print(text)

# print only duplicate in python string
text = "arun kumar"
duplicates_string = []
for item in text:
    if item not in duplicates_string:
        duplicates_string.append(item)
    else:
        print(item)

# string replace * in python
word = "arun kumar"
words = word.split()
words[1] = words[1].replace("a","*")
result = " ".join(words)
print(result)

# duplicate in python int
duplicate = [1,2,3,4,1,2,3,4,6,7,8,9]
duplicate_int = []
for item in duplicate:
    if item not in duplicate_int:
        duplicate_int.append(item)
print(duplicate_int)

# max number in python
a = [1,2,3,4,5,400,21,33,11]
max = a[0]
for item in a:
    if item > max :
        max = item
print(max)

# Second Max number in python
a = [1, 2, 3, 4, 5, 400, 21, 33, 11]
max = a[0]
second_max = float('-inf')

for item in a:
    if item > max:
        second_max = max
        max = item
    else:
        if item != max:
            if item > second_max:
                second_max = item
print(second_max)

# min number in python
a = [1,2,3,4,5,67,8,9,]
min = a[0]
for item in a:
    if item < min:
        min = item
print(min)

# add number in python
a = [1,2,3,4,5,6,7,8,9]
total = 0
for item in a:
    total = item + total
print(total)

# pattern in python
for i in range(6,0,-1):
    for j in range(1, i+1):
        print("*", end='')
    print()

# pattern in python alphabet
ch = ord("D")
for i in range(4,0,-1):
    for j in range(i):
        print(chr(ch),end='')
    print()
    ch-=1

# swap number
a = 5
b = 10
a,b = b,a
print("a:",a)
print("b:",b)


# covert list and set value in single dictionary
fruits = ["apple","orange"]
number = {1,2}
result = dict(zip(fruits,number))
print(result)

# split function in python
a = "Python Testing"
x = a.split()
print(x[1],x[0])

# Program to Print 'f' from the String python
a = "aaaabbbcccccccedddfgghhhh"
for char in a:
    if char == 'f':
        print(char)

# python dictionary
dict = {"name": "Arun", "age": 30}
for key, value in dict.items():
    print(f"{key}:{value}")

#*args and **kwargs
def func(*args,**kwargs):
    print(args)
    print(kwargs)

func(1,2 ,name="arun",age="kumar")

# Calculate average price
products = [
    {"product": "dell", "company": "HCL", "price": 50},
    {"product": "Acer", "company": "Tata", "price": 150},
    {"product": "iPad", "company": "iPhone", "price": 250}
]
total_price = 0
for item in products:
    total_price = total_price + item["price"]
    average_price = total_price/len(products)
print(f"Average_price:",average_price)

# Write a Python function that returns the sum of all even numbers in a given list.
# Input: [1, 2, 3, 4, 5, 6]
# Output: 12
numbers = [1, 2, 3, 4, 5, 6]
even_sum = 0
for item in numbers:
    if item % 2 == 0:
        even_sum = even_sum + item
print(even_sum)

# Write a Python function that returns a new list containing only the odd numbers from the given list.
# 	Input: [1, 2, 3, 4, 5, 6]
# 	Output: [1, 3, 5]

odd = [1, 2, 3, 4, 5, 6]
odd_number = []
for num in odd:
    if num % 2 !=0:
        odd_number.append(num)
print(odd_number)

# Write a Python function that takes a list of numbers and returns the largest and smallest number in the list.
# 	Input: [5, 10, 3, 8, 2]
# 	Output: (10, 2)

def find_number(numbers):
    max_nums = numbers[0]
    min_nums = numbers[0]

    for num in numbers:
        if num > max_nums:
            max_nums = num
        if num < min_nums:
            min_nums = num
    return (max_nums, min_nums)

numbers = [5, 10, 3, 8, 2]
small = find_number(numbers)
print(small)

# Write a Python function that takes a list of numbers and returns the count of positive, negative, and zero values.
# 	Input: [2, -1, 0, 5, -3, 0, 4]
# 	Output: (3, 2, 2)

def count_numbers(numbers):
    positive = 0
    negative = 0
    zero = 0

    for num in numbers:
        if num > 0:
            positive = positive + 1
        elif num < 0:
            negative = negative + 1
        else:
            zero = zero + 1
    return (positive, negative, zero)

input_list = [2, -1, 0, 5, -3, 0, 4]
result = count_numbers(input_list)
print(result)


# Count vowels and consonants in the string "Data Science is fun!" and print the counts.

word = "data science is fun!"
vowels = "aeiou"
count = 0
for item in word:
    if item in vowels:
        count = count + 1
print(count)

# print the common elements between two lists and the different elements from the first list.

list1 = ["admin","admin"]
list2 = ["admin","admin@123"]

original = []
duplicate = []
for item in list2:
    if item in list1:
            original.append(item)
    else:
        duplicate.append(item)

print(duplicate)
print(original)

# Write a Python function that takes a list of numbers and returns a new list containing only the even numbers from the original list.
number = [2,4,3,6,9,7,10,1,5]
num = len(number)
for i in range(num):
    for j in range(i+1,num):
        if number[i] > number[j]:
            number[i],number[j] = number[j],number[i]
print(number)

# Given a list of integers, print the numbers that appear more than three times in the list.
numbers = [1, 2, 6, 7, 8, 3, 3, 3, 5, 9, 6, 6, 6, 2, 2, 2]
word = {}

for item in numbers:
    if item in word:
        word[item] += 1
    else:
        word[item] = 1

for key, count in word.items():
    if count >= 3:
        # This will print the key repeated 3 times (e.g., 3,3,3)
        print(f"{key},{key},{key}")

# Write a Python function that takes a list of numbers and moves all the zeros to the end of the list while maintaining the order of the non-zero elements.
number = [1,0,2,3,0,4,6,0]
output = []
zeros = []
for item in number:
    if item >=1:
        output.append(item)
    else:
        zeros.append(item)
text = output + zeros
print(text)



