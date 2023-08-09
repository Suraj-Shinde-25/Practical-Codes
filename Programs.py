# 1. Write a Python program to check whether the no is even and odd.

n = int(input("Enter a number:"))
if (n % 2 == 0):
    print(n, "is even number")
else:
    print(n, "is odd number")

# 2. Write a Python program to display Greater no between 3 inputs.

a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))
if a > b and a > c:
    print(a, "is largest")
elif b > a and b > c:
    print(b, "is largest")
else:
    print(c, "is largest")

# 3. Write a Python program to print prime no between n and m.

n = int(input("Enter lower range:"))
m = int(input("Enter upper range:"))
l = []
print("The Prime numbers in the range are:")
for i in range(n, m+1):
    count = 0
    for j in range(1, i+1):
        if i % j == 0:
            count += 1
    if count == 2:
        l.append(i)
print(l)

for num in range(n, m+1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
            else:
                print(num)

# 4.Write a Python program to display Fibonacci series.
# Write function in python for the Fibonacci Series

def fib(n):

    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    print(result)


n = int(input("Enter a range:"))
fib(n)

# 5. Write a Python program factorial of no.

n = int(input("Enter a number:"))
fact = 1
if n < 0:
    print(n, "Factorial of negative number doesn't exist")
elif n == 0:
    print(n, "factorial is 1")
else:
    for i in range(1, n+1):
        fact = fact*i
    print("The factorial of number", n, "is", fact)

# 6.Write a Python script to generate and print a dictionary that contains a
# number (between 1 and n) in the form (x, x*x).

# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

n = int(input("Enter a number:"))
d = dict()
for x in range(1, n+1):
    d[x] = x*x
print(d)

# 7.Write a Python script to concatenate following dictionaries to create a new one.
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
dic4 = {}
for d in (dic1, dic2, dic3):
    dic4.update(d)
print("Updated Dictionary:", dic4)

# 8.Write a Python program to perform star pattern.
# *
# **
# ***
# ****

n = int(input("Enter rows:"))
for row in range(0, n):
    for col in range(0, row+1):
        print("*", end="")
    print()

# 9. Write a Python program to perform star Pattern.
# ****
# ***
# **
# *

n = int(input("Enter no. of rows:"))
for row in range(n):
    for col in range(n-row):
        print("*", end="")
    print()

# 10.Write a Python program to construct the following pattern, using a nested loop number.
# 687954231
# 87954231
# 7954231
# 954231
# 54231
# 4231
# 231
# 31
# 1

n = int(input("Enter no. of rows:"))
num = 9
for row in range(1, n+1):
    for col in range(num, 0, -1):
        if (col == 9):
            col = 6
        elif (col == 6):
            col = 9
        elif (col == 3):
            col = 2
        elif (col == 2):
            col = 3
        print(col, end="")
    num = num-1
    print()

# 11.Write a Python program to get a string from a given string where all
# occurrences of its first char have been changed to '$', except the first char itself
# 
# Sample String : 'restart'
# Expected Result : 'resta$t'

def func1():
    str1 = input("Enter a string:")
    char = str1[0]
    str1 = str1.replace(char, '$')
    str1 = char + str1[1:]
    print(str1)


func1()

# 12.Write a Python program to remove the characters which have odd index values of a given string


def remov():
    str = input("Enter a string: ")
    i = 0
    new_str = ' '
    while i < len(str):
        new_str += str[i]
        i += 2
    return new_str


print("String after removing all odd index values:", remov())

# 13. Write a Python program to get a string made of the
# first 2 and the last 2 chars from a given a string.
# If the string length is less than 2, return instead of the empty string

# Sample String : “Welcome to DYPSOMCA”
# Expected Result : WeCA
# Sample String : 'We'
# Expected Result : 'WeWe'
# Sample String : ' w'
# Expected Result : Empty String

def func1(str):
    if len(str) < 2:
        return 'Empty string'
    return str[0:2]+str[-2:]


print(func1('Welcome to DYSOMCA'))
print(func1('We'))
print(func1('w'))

# 14.Write a Python class to implement pow(x, n).

class solution:
    def pow(self, x, n):
        if x == 0 or x == 1 or n == 1:
            return x
        if x == -1:
            if n % 2 == 0:
                return 1
            else:
                return -1
        if n == 0:
            return 1
        if n < 0:
            return 1/self.pow(x, -n)
        val = self.pow(x, n//2)
        if n % 2 == 0:
            return val*val
        return val*val*x


print(solution().pow(2, -6))
print(solution().pow(3, 10))

# 15. Write a Python class named Circle constructed by a radius and
# two methods which will compute the area and the perimeter of a circle.

class Circle:
    def __init__(self, r):
        self.rad = r

    def area(self):
        area = 3.14*self.rad*self.rad
        print("Area of Circle:", area)

    def peri(self):
        per = 2*3.14*self.rad
        print("Perimeter:", per)


obj = Circle(9)
obj.area()
obj.peri()

# 16. Write a Python program to get the
# factorial of a non-negative integer using recursion.

def fact(n):
    if n == 0:
        return 1
    elif n < 0:
        print("Number can't be negative")
    else:
        return n*fact(n-1)


n = int(input("Enter a number:"))
print("Factorial of", n, "is", fact(n))

# 17. Write a Python program to read first n lines of a file

f = open("book.txt", "r")
l = f.readlines()
x = int(input("Enter a no. of lines:"))
n = l[:x]
print(n)

# 18. Write a Python program to read a file line by line store it into a variable.

f = open("book.txt", "r")
data = f.readlines()
print(data)
s =data
print(s)


# 19.Write a Python program to combine each line
# from first file with the corresponding line in second file.

def comblines():
    f1 = open("File1.txt", "r")
    f2 = open("File2.txt", "r")
    f3 = open("Merge.txt", "w")
    lines1 = f1.readlines()
    lines2 = f2.readlines()
    for i in range(len(lines1)):
        merge = lines1[i]+lines2[i]
        f3.write(merge)
    f1.close()
    f2.close()
    f3.close()
    print("Data written to a Merge.txt successfully!!!")


comblines()

# 20.Write a program in which you need to calculate size of rectangle,
# square, circle and Triangle.(Separate Package need to be created for the same)

cal.py
demo.py

# 21. Write a program for Decorator and Generator.

# Decorator
def first(msg):
    print(msg)


def second(func, msg):
    func(msg)


second(first, "Hello!")

# Generator


def even_iterator():
    n = 0
    n += 2
    yield n
    n += 2
    yield n
    n += 2
    yield n


num = even_iterator()
print(next(num))
print(next(num))
print(next(num))

# 22. Write a program to validate URL using regular expression.   

import re


def validateURL(url):
    regex = "^((http|https)://)[-a-zA-Z0-9@:%.\\+~#?&//=]{2,256}\\.[a-z]{2,6}\\b([-a-zA-Z0-9@:%.\\+~#?&//=]*)$"
    r = re.compile(regex)

    if (re.search(r, url)):
        print("Valid")
    else:
        print("Not Valid")


url1 = input("Enter an URL:")
validateURL(url1)


# 23. Write a program to validate email using regular expression. 

import re
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'


def check(email):
    if (re.search(regex, email)):
        print('Valid Mail Address')
    else:
        print('Invalid Mail Address')


if __name__ == '__main__':
    email = input("Enter Email:")
    check(email)


# 24. Write a program to validate Password using regular expression.
# Condition
# 1. Minimum length of password: 8 characters
# 2. Atleast one alphabet must bewteen [a-z]
# 3. Atleast one alphabet should be of uppercase [A-Z]
# 4. Atleast 1 number or digit between [0-9]
# 5. Atleast 1 charcter from [$,@,#]

import re


def main():
    lower = re.compile(r'[a-z]')
    upper = re.compile(r'[A-Z]')
    number = re.compile(r'\d')
    special = re.compile(r'[$#@]')
    password = input("Enter a password:")
    if len(password) < 8:
        print("Password length should be more than 8 characters!!!")
    if not lower.search(password):
        print("Password should consist atleast one lowercase letter!!!")
    if not upper.search(password):
        print("Password should consist atleast one uppercase letter!!!")
    if not number.search(password):
        print("Password should consist atleast one number!!!")
    if not special.search(password):
        print("Password should consist atleast one special character")
    else:
        print("Valid Password!!!")


if __name__ == '__main__':
    main()

# 25.Write a program that ask for an integer number.
# Accepted number should be in between 1 to 10 and break the loop if not then generate the exception and print an error message.

while True:
    try:
        n = int(input("Enter a number:"))
        if n > 10 or n < 1:
            raise Exception
        else:
            print("Number is within range")
            break
    except Exception:
        print("Number should be between 1 to 10")

# 26. Write a Python Program to perform synchronized Multi-threading.

from threading import *
import time

l = Lock()

def wish(name, age):
    for i in range(2):
        l.acquire()
        print("Hi", name)
        time.sleep(2)
        print("Your age is:", age)
        l.release()


t1 = Thread(target=wish, args=("Suraj", 23))
t2 = Thread(target=wish, args=("Tony", 30))
t1.start()
t2.start()

# 27. Write a Program for Performing basic CRUD operations with MongoDB and python.

import pymongo
db = pymongo.MongoClient("mongodb://localhost:27017/")
database = db["Employee3"]
collection = database["EmployeeDetails"]
while True:
    print("\nMAIN MENU")
    print("1.Insert")
    print("2.Update")
    print("3.Delete")
    print("4.Display")
    print("5.Exit")
    choice1 = int(input("Enter the Choice:"))

    if choice1 == 1:
        a = input("Enter your name:")
        b = input("Enter your address:")
        dict1 = {"name": a, "address": b}
        collection.insert_one(dict1)
        print("Data Entered Successfully!!")

    elif choice1 == 2:
        while True:
            print("\nUpdate Details of?")
            print("1.Name")
            print("2.Address")
            print("3.Exit")
            choice2 = int(input("Enter your choice:"))

            if choice2 == 1:
                a = input("Enter your previous name:")
                b = input("Enter your name to be updated:")

                prev = {"name": a}
                nextt = {"$set": {"name": b}}
                collection.update_one(prev, nextt)
                print("Name Updated Successfully!!")

            elif choice2 == 2:
                a = input("Enter your name:")
                b = input("Enter your address to be updated:")

                prev = {"name": a}
                nextt = {"$set": {"address": b}}
                collection.update_one(prev, nextt)
                print("Address Updated Successfully!!")

            elif choice2 == 3:
                break

    elif choice1 == 3:
        a = input("Enter the record to be deleted:")
        d = {"name": a}
        collection.delete_one(d)
        print('Record Deleted Successfull!!')

    elif choice1 == 4:
        x = collection.find()
        for i in x:
            print(i)

    elif choice1 == 5:
        break


# 28. Write a Program Create Numpy Array with Random Values – numpy.random.rand()

import numpy as np

array = np.random.rand(2, 2)
print("\nArray filled with random value:", array)

# 29. Write a Program Numpy array and Reverse the Array.

import numpy as np

x = np.arange(10, 21)
print("Original Array:")
print(x)
print("Reverse Array:")
x = x[::-1]
print(x)

# 30. Write a Programs for series and data frames.

Series
import pandas as pd
import numpy as np
arr = np.array([2, 4, 6, 7, 10, 20])
si = pd.Series(arr)
print(si)

# Data Frames
s1 = pd.Series([1, 2, 3])
s2 = pd.Series([70, 80, 60])
s3 = pd.Series(['Varad', 'Yogesh', 'Mayank'])
data = {'RollNo': s1, 'Marks': s2, 'Name': s3}
dt = pd.DataFrame(data)
print(dt)

# 31. Write a Program for data visualization using Matplotlib.

# Line Chart
from matplotlib import pyplot as plt
x = [2, 4, 8, 10]
y = [8, 5, 9, 12]
plt.xlabel('x-Axis')
plt.ylabel('y-Axis')
plt.title("Line Chart")
plt.plot(x, y)
plt.show()

# Bar Graph
x = [2, 4, 8, 10]
y = [8, 5, 9, 12]
plt.title("Bar Graph")
plt.bar(x, y)
plt.show()

# Pie Chart
x = [2, 4, 8, 10]
plt.title("Pie Chart")
plt.pie(x)
plt.show()

# Scatter plot
x = [2, 4, 8, 10]
y = [8, 5, 9, 12]
plt.title("Scatter Plot")
plt.scatter(x, y)
plt.show()

# Histogram
x = [2, 4, 8, 10]
plt.title("Histogram")
plt.hist(x)
plt.show()
