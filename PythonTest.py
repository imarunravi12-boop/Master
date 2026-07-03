import copy
from copy import deepcopy

# 1.Real time example using decorator

# Decorator function to log access
def log_access(func):
    def wrapper(name, role):
        print(f"Accessing system as {name}")
        return func(name,role)
    return wrapper
# Function to greet user, wrapped with the decorator
@log_access
def greet_user(name, role):
    print(f"Welcome {name}! as an {role}")

# call function
greet_user("arun","admin")

# 2.With arguments
def decorator(fun):
    def add_function(a, b):
        print(f"adding {a} and {b}")
        return fun(a, b)
    return add_function
@decorator
def add(a, b):
    print(a + b)
(add(5, 5))


# 3.Decorator to Print User Access Level
def access_level(func):
    def wrapper(name, role):
        print (f"Welcome {name}! as a admin")
        return func(name,role)
    return wrapper

@access_level
def greet_user(name, role):
    print(f"Welcome {role}! as a user")  # Function logic handled in decorator

# Outputs
(greet_user("Rohit", "Jeevanithin"))

# 5. Handle String Input and Convert to Numerical Type
a = input("Enter the number A:")
b = input("Enter the number B:")

avg = (float(a) + float(b))/2
print("Average:",avg)

# 6.staticmethod class in python
class person:
    @staticmethod
    def add(a,b):
        return a + b
print(person.add(2,8))


# 7.Class method class in python
class company:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def coporate(self):
        print(f"Name:",self.name)
        print(f"Id:",self.id)

mnc = company("Arun",1260)
mnc.coporate()


# 8. Count vowels in a string
string = "python automation testing"
vowels = "aeiou"
count = 0

for char in string:
    if char in vowels:
        count = count + 1
print(f"Vowels Count :",count)


# 9.Find even and odd numbers
number = [10,15,20,25,30,35,40,45,50]
even = []
odd = []
for item in number:
    if item % 2 == 0:
        even.append(item)
    else:
        odd.append(item)
print(f"Even Numbers:",even)
print(f"Odd Numbers:",odd)

# 10. swap two numbers without using third variable
a = 5
b = 10
a,b = b,a
print(f"A:",a)
print(f"B:",b)

# 12 . Merge two lists
list1 = [1,2,3,4]
list2 = [5,6,7,8]
merge_list = list1 + list2
print(f"Final List:",merge_list)




