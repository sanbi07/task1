# 1
numbers = []
while True:
    num = int(input("Enter number: "))
    if num in numbers:
        print("Duplicate found")
        break
    numbers.append(num)

# 2
num = int(input("Enter a positive integer: "))
fact = 1
while num > 0:
    fact *= num
    num -= 1
print(fact)

# 3
num = int(input("Enter a number: "))
total = 0
i = 1
while i <= num:
    total += i
    i += 1
print(total)

# 4
numbers = [5, 10, 20, 10, 30, 10]
target = 10
count = 0
i = 0
while i < len(numbers):
    if numbers[i] == target:
        count += 1
    i += 1
print(count)

# 5
sentence = input("Enter a sentence: ")
vowels = consonants = 0
i = 0
while i < len(sentence):
    ch = sentence[i].lower()
    if ch.isalpha():
        if ch in "aeiou":
            vowels += 1
        else:
            consonants += 1
    i += 1
print("Vowels:", vowels)
print("Consonants:", consonants)

# 6
num = abs(int(input("Enter an integer: ")))
count = 0
while num > 0:
    count += 1
    num //= 10
print(count)

# 7
n = int(input("Enter number: "))
while n != 1:
    print(n, end=", ")
    if n % 2 == 0:
        n //= 2
    else:
        n = n * 3 + 1
print(1)

# 8
ch = ord('A')
while ch <= ord('Z'):
    print(chr(ch), end=" ")
    ch += 1

# 9
start = int(input("Start: "))
end = int(input("End: "))
while start <= end:
    print(start)
    start += 1

# 10
num = 49
while num >= 1:
    print(num)
    num -= 2

# 11
num = 7
while num <= 100:
    print(num)
    num += 7

# 12
total = 0
while True:
    num = int(input("Enter number: "))
    if num == 0:
        break
    total += num
print(total)

# 13
age = int(input("Enter age: "))
while age < 0 or age > 120:
    print("Invalid age")
    age = int(input("Enter age again: "))
print("Valid age")

# 14
total = count = 0
while True:
    score = float(input("Enter score: "))
    if score == -1:
        break
    total += score
    count += 1
print("Average =", total / count)

# 15
password = "secret123"
attempts = 0
while attempts < 3:
    user = input("Enter password: ")
    if user == password:
        print("Access Granted")
        break
    attempts += 1
else:
    print("Access Denied")

# 16
num = int(input("Enter integer: "))
reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10
print(reverse)

# 17
n = int(input("Enter terms: "))
a, b = 0, 1
count = 0
while count < n:
    print(a, end=" ")
    a, b = b, a + b
    count += 1

# 18
text = input("Enter string: ")
result = ""
i = 0
while i < len(text):
    if text[i].lower() not in "aeiou":
        result += text[i]
    i += 1
print(result)

# 19
text = input("Enter string: ")
count = 0
i = 0
while i < len(text) - 1:
    if text[i:i+2] == "hi":
        count += 1
    i += 1
print(count)

# 20
numbers = [12, 25, 7, 30, 18, 40, 55, 9]
i = 0
while i < len(numbers):
    if numbers[i] % 5 == 0:
        print(numbers[i])
    i += 1

# 21
text = input("Enter string: ")
result = ""
i = 0
while i < len(text):
    if text[i].islower():
        result += text[i].upper()
    elif text[i].isupper():
        result += text[i].lower()
    else:
        result += text[i]
    i += 1
print(result)

# 29
def count_case(text):
    upper = lower = 0
    i = 0
    while i < len(text):
        if text[i].isupper():
            upper += 1
        elif text[i].islower():
            lower += 1
        i += 1
    print("No. of upper case characters :", upper)
    print("No. of lower case characters :", lower)

count_case('The quick Brow Fox')

# 30
while True:
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 4:
        break

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    if choice == 1:
        print(a + b)
    elif choice == 2:
        print(a - b)
    elif choice == 3:
        print(a * b)

# 31
positive = negative = 0
while True:
    num = int(input("Enter number: "))
    if num == 0:
        break
    if num > 0:
        positive += 1
    else:
        negative += 1
print("Positive:", positive)
print("Negative:", negative)

# 32
start = int(input("Start: "))
end = int(input("End: "))

while start <= end:
    num = start
    if num > 1:
        i = 2
        prime = True
        while i < num:
            if num % i == 0:
                prime = False
                break
            i += 1
        if prime:
            print(num)
    start += 1

# 33
numbers = [12, 40, 21, 31, 10, 7, 5]
i = 0
while i < len(numbers):
    if numbers[i] < 20:
        print(numbers[i])
    i += 1

# 34
numbers = [45, 60, 12, 75, 30, 55, 8, 90]
i = 0
while i < len(numbers):
    if numbers[i] > 50:
        numbers[i] = 0
    i += 1
print(numbers)

# 35
numbers = [15, 25, 30, 45, 60, 12, 90, 7]
count = 0
i = 0
while i < len(numbers):
    if numbers[i] % 3 == 0 and numbers[i] % 5 == 0:
        count += 1
    i += 1
print(count)

# 36
numbers = [10, 15, 25, 30, 45]
i = 0
sorted_list = True
while i < len(numbers) - 1:
    if numbers[i] > numbers[i + 1]:
        sorted_list = False
        break
    i += 1

if sorted_list:
    print("Sorted")
else:
    print("Not Sorted")

# 37
ch = ord('a')
while ch <= ord('z'):
    print(chr(ch), end=" ")
    ch += 1

# 38
pages = [45, 30, 50, 40]
i = 0
chapter = 1
while i < len(pages):
    print(f"Chapter {chapter} has {pages[i]} pages")
    chapter += 1
    i += 1

# 39
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

i = 0
while i < len(list1):
    if list1[i] in list2:
        print(list1[i])
    i += 1

# 40
tables = [2, 4, 6, 7, 8]
i = 0
while i < len(tables):
    j = 1
    while j <= 10:
        print(f"{tables[i]} x {j} = {tables[i] * j}")
        j += 1
    print()
    i += 1

# 41
numbers = [1, 2, 3, 4, 2]
i = 0
duplicate = False

while i < len(numbers):
    j = i + 1
    while j < len(numbers):
        if numbers[i] == numbers[j]:
            duplicate = True
            break
        j += 1
    if duplicate:
        break
    i += 1

if duplicate:
    print("Has Duplicates")
else:
    print("No Duplicates")