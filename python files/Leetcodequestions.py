# 1.Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# Input: nums = [2,7,11,15],
# target = 9
# Output: [0,1]
from importlib.resources.readers import remove_duplicates

number = [2,7,11,15]
target = 9
for i in range(len(number)):
    for j in range(i+1,len(number)):
        if number[i] + number[j] == target:
            print(f"Pair index:{i},{j}")

# 2.Add Two Numbers represented as Linked Lists
# Input: s = "abcabcbb"
# Output: 3
word = "abcabcbb"
remove_duplicates = []
for item in word:
    if item not in remove_duplicates:
        remove_duplicates.append(item)
text = len(remove_duplicates)
print(text)

# 3.Palindrome Number
def is_palindrome(x):
    return str(x) == str(x)[::-1]

print(is_palindrome(121))
print(is_palindrome(-121))

def is_palindrome(x):
    return x == x[::-1]

print(is_palindrome("madam"))   # True
print(is_palindrome("python"))  # False

# 4.Reverse the digits of a number while keeping the sign intact.
num = "-123"
if num[0] == "-":
    number = "-" + num[:0:-1]
else:
    number = num[::-1]
print(number)

def number(words):
    if words[0] == "-":
        return  "-" + words[:0:-1]
    else:
        return words[::-1]
words = "-123"
word = number(words)
print(word)

# 5. Find the median of two sorted arrays.
# Input: nums1 = [1,3],
# nums2 = [2]
# Output: 2.00000

num1 = [1,3]
num2 = [2]
merged = sorted(num1 + num2)
length = len(merged)
if length % 2 == 0:
    median = (merged[length//2 - 1] + merged[length//2]) / 2
else:
    median = merged[length//2]
print(median)
