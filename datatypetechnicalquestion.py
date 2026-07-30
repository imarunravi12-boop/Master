# 1.Sort the list and then add number 12 at the end.
nums = [10, 5, 8, 3]
nums.sort()
nums.append(12)
print(nums)

# Q2.Inserting and Removing
# Insert "orange" at index 1.
# Remove "banana" from the list.
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "orange")   # index 1 means after "apple"
fruits.remove("banana")
print(fruits)

# Q3. Pop and Reverse
# Remove the last element using pop and store it in a variable.
# Reverse the list.
letters = ["a", "b", "c", "d"]
word = letters.pop()
print("Popped element:", word)
letters.reverse()
print(letters)

# Q4. Copy and Clear
# Make a copy of the list and store it in another variable.
# Clear the original list.
data = [1, 2, 3, 4]
datas = data.copy()
datas.clear()
print("Copied list:", datas)
print("Original list after clear:", data)

# Q5. Split and Join
# Split the string into words.
# Join the words with "-" as separator.
# Expected: "Python-is-fun"
sentence = "Python is fun"
word = sentence.split()
result = "-".join(word)
print(result)

# Q6. Replace and Upper
# Replace "java" with "Python".
# Convert the string to uppercase.
text = "I like java"
word = text.replace("java","python")
print(word.upper())

# Q7. Strip and Count
# Remove spaces from start and end.
# Count how many times "l" appears.
line = "   hello world   "
words = line.strip()
print(words)
clean = line.count("l")
print(clean)

# Q8. Startswith and Find
# Check if word starts with "auto".
# Find the position of "test".
word = "automation testing"
print(word.startswith("auto"))
print(word.find("test"))

# Q9. List Sort with sorted()
# Use sorted() (not .sort) to create a new sorted list.
# Print both original and new list.
nums = [50, 20, 40, 10, 30]
nums.sort()
print("Sorted list:", word)


# Q10. Append + Extend
# Add number 5 to list a using append.
# Add all items of b to list a using extend.
a = [1, 2]
b = [3, 4]
a.append(5)
a.extend(b)
print(a)

# Q11. Pop Specific Index
# Pop the element at index 2 and store it in a variable.
# Print the popped value and the updated list.
letters = ["x", "y", "z", "w"]
popped_value = letters.pop(2)
print("Popped value:", popped_value)

# Q12. Reverse with reversed()
# Use the reversed() function to reverse (don’t use .reverse()).
# Convert the result into a list and print it.
data = [100, 200, 300]
reverse = list(reversed(data))
print(reverse)

# Q13. String Split + Count
# Split the string into words.
# Count how many times "Python" appears.
sentence = "Python Python Java C++ Python"
words = sentence.split()
count = words.count("Python")
print(count)

# Q14. Replace + Title
# Replace "python" with "Java".
# Convert the string to Title Case (each word capitalized).
text = "welcome to python programming"
word = text.replace("python","java")
print(word.title())

# Q15. Find + Slice
# Find the index of "Python".
# Print the substring from "Python" to the end.
line = "Learning Python is fun"
index = line.find("Python")
print(index)

# Q16. Join + Upper
# Join the words with "_" separator.
# Convert the final string to uppercase.
words = ["data", "science", "rocks"]
result = "_".join(words)
print(result.upper())

# Q.17 Fruits List Manipulation
# Add "mango" at the END of the list
# Then add "orange" at the BEGINNING of the list
# Print the final list
fruits = ["apple", "banana", "cherry"]
word = fruits.append('mango')
fruits.insert(0,"orange")
print(fruits)

# Q.18 Colors List Manipulation
# Remove "green" from the list
# Then remove the LAST element of the list
# Print the final list
colors = ["red", "green", "blue", "yellow"]
colors.remove("green")
colors.pop()
print(colors)

# Q.19 Numbers List Manipulation
# Double each number in the list using a loop
# Store results in a new list
# Print the new list
numbers = [1, 2, 3, 4, 5]
number = []
for item in numbers:
    number.append(item*2)
print(number)

# Q.20 Words List Manipulation
# Convert each word to uppercase
# Store them in a new list
# Print the new list
words = ["python", "java", "c++", "ruby"]
word_number = []
for item in words:
    word_number.append(item.upper())
print(word_number)

# Q.21 Sum of Numbers
# Find the sum of all numbers in the list
# Print the result
nums = [3, 6, 9, 12, 15]
total = 0
for item in numbers:
    total = item + total
print(total)

# Q.22 Sentence Word Count
# Split the sentence into words
# Print how many words are in the sentence
sentence = "I love learning Python"
words = sentence.split()
print(len(words))

# Q.23 String Manipulation
# Convert all letters to uppercase
# Then check if the text starts with "HEL"
# Print both results
text = "hello world"
words =text.upper()
print(words)
print(words.startswith("HEL"))

# Q.24 Longest Word Finder
# Find the longest word in the list
# Print the word and its length
words = ["cat", "dog", "elephant", "ant"]
longest_word = []
for item in words:
    if len(item) > len(longest_word):
        longest_word = item
print(longest_word)

# Q.25 Letter Count in Sentence
# Count how many times the letter "o" appears
# Print the result
sentence = "Python is powerful and easy"
count = sentence.count('o')
print(count)

# Q.26 Filter Fruits by Length
# Create a new list that contains only fruits with names longer than 5 letters
# Print that new list
fruits = ["apple", "banana", "mango", "kiwi"]
fruit = []
for item in fruits:
    if len(item) > len(fruit):
        fruit.append(item)
print(fruit)

# Q.27 Average of Numbers
# Calculate the average (mean) of the numbers
# Print the result
numbers = [1, 2, 3, 4, 5]
total = 0
for item in numbers:
    total = item + total
    avg =total/len(numbers)
print(avg)

# Q.28 Longest Word in Text
# Split the text into words
# Print the longest word in the text
text = "Python programming is amazing"
words=text.split()
lengest_word = max(words, key=len)
print(lengest_word)

# Q.29 String Replacement
# Replace the word "fun" with "awesome"
# Print the updated sentence
sentence = "Learning Python is fun"
word = sentence.replace("fun","awesome")
print(word)

# Q.30 Reverse List
# Reverse the list (without using reverse() method)
# Print the reversed lis
nums = [10, 20, 30, 40, 50]
number = list(reversed(nums))
print(number)

# Q.31 Join Words with Comma
# Join the words into a single string with commas separating them
# Print the resulting string
words = ["red", "green", "blue"]
result = ",".join(words)
print(result)

# Q.32 Count Specific Letter
# Count how many times the letter "a" appears in the text
# Print the result
text = "Data analysis is an art"
count = text.count("a")
print(count)

# Q.33 Sort Numbers
# Sort the numbers in ascending order
# Print the sorted list
numbers = [42, 23, 16, 15, 8, 4]
numbers.sort()
print(numbers)

# Q.34 Capitalize Words
# Convert the first letter of each word to uppercase
# Print the updated sentence
sentence = "hello world from python"
words = sentence.title()
print(words)

# Q.35 Find Index of Word
# Find the index of the word "python" in the text
# Print the index
text = "I love python programming"
index = text.find("python")
print(index)

# Q.36 Remove Duplicates from List
# Create a new list with duplicates removed
# Print the new list
Number = [1, 2, 2, 3, 4, 4, 5]
duplicate = []
for item in Number:
    if item not in duplicate:
        duplicate.append(item)
print(duplicate)

# Q.37 Count Even and Odd Numbers
# Count how many numbers are even and how many are odd
# Print both counts
numbers = [10, 15, 20, 25, 30]
even_count = 0
odd_count = 0
for item in numbers:
    if item % 2 ==0:
        even_count = even_count + 1
    else:
        odd_count = odd_count + 1
print(f"Even count: {even_count}, Odd count: {odd_count}")

# Q.38 Find Minimum and Maximum
# Find the smallest and largest number in the list
# Print both numbers
def maxmin_number(numbers):
    max_number = numbers[0]
    min_number = numbers[0]

    for item in numbers:
        if item > max_number:
            max_number = item
        if item < min_number:
            min_number = item
    return (max_number, min_number)

numbers = [34, 1, 23, 4, 3, 78, 56]
nums = maxmin_number(numbers)
print(nums)

# Q.39 Filter Words by Length
# Create a new list with words longer than 3 letters
# Print the new list
words = ["it", "is", "a", "sunny", "day"]
word = []
for item in words:
    if len(item) > 3:
        word.append(item)
print(word)

# Q.40 Calculate Product of Numbers
# Calculate the product of all numbers in the list
# Print the result
numbers = [1, 2, 3, 4]
product = 1
for item in numbers:
    product = product * item
print(product)

# 41. Find Substring in Text
# Check if the substring "data" is in the text
# Print True or False
text = "Data science is fun"
print("data" in text.lower())

