
# 1. Even or Odd from 1 to 5

for i in range(1, 6):
    if i % 2 == 0:
        print(f"Number {i} is even.")
    else:
        print(f"Number {i} is odd.")

# 2. Sum of all elements in a list

lst = [10, 20, 30, 40]

total = 0

for i in lst:
    total = total + i
    print(f"Added {i}. Running total is {total}.")

print("------------------------------")
print(f"Total Sum: {total}")

# 3. Email greetings

student_names = ["Ram", "Hari", "Sita"]

print("--- Email Greetings Generated ---")

for name in student_names:
    print(f"Hi {name}, your course approval is ready!")

# 4. Book chapter summary

pages = [45, 30, 50, 40]

print("--- Book Chapter Summary ---")

for i in range(len(pages)):
    print(f"Chapter {i+1} has {pages[i]} pages.")

# 5. Product of all elements

lst = [4, 5, 3, 2]

product = 1

for i in lst:
    product = product * i

print("Product =", product)

# 6. Multiplication table of 11

number = 11

for i in range(1, 11):
    print(number, "x", i, "=", number * i)

# 7. Reverse a list

lst = [3, 2, 1, 4, 5]

reversed_list = []

for i in lst[::-1]:
    reversed_list.append(i)

print(reversed_list)

# 8. Common elements in two lists

a = [1, 2, 3, 4, 5]
b = [3, 4, 5, 6, 7]

for i in a:
    if i in b:
        print(i)

# 9. Print 1 and 4 only

lst = [1, 2, 3, 4]

for i in lst:
    if i == 1 or i == 4:
        print(i)

# 10. Remove vowels from a string

text = "programming"

vowels = "aeiouAEIOU"
result = ""

for i in text:
    if i not in vowels:
        result += i

print(result)

# 11. Count vowels and consonants

text = "Loops are Fun"

vowels = 0
consonants = 0

for i in text.lower():
    if i.isalpha():
        if i in "aeiou":
            vowels += 1
        else:
            consonants += 1

print("vowels:", vowels)
print("consonants:", consonants)


# 12. Separate odd and even numbers

lst = [1, 2, 3, 4, 5]

odd = []
even = []

for i in lst:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print("Odd:", odd)
print("Even:", even)


# 13. Prime number check

num = 7

count = 0

for i in range(1, num + 1):
    if num % i == 0:
        count += 1

if count == 2:
    print("Prime Number")
else:
    print("Not Prime")


# 14. Append datatypes to separate lists

lst = [1, 2, 3, 4, "a", "b"]

int_list = []
str_list = []

for i in lst:
    if type(i) == int:
        int_list.append(type(i))
    else:
        str_list.append(type(i))

print(int_list)
print(str_list)


# 15. Count digits and letters

text = "Python123"

letters = 0
digits = 0

for i in text:
    if i.isalpha():
        letters += 1
    elif i.isdigit():
        digits += 1

print("Letters:", letters)
print("Digits:", digits)


# 16. Username and password validation

username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print("Valid User")
else:
    print("Invalid User")


# 17. Odd or even

num = 10

if num % 2 == 0:
    print("Even")
else:
    print("Odd")


# 18. Factorial of a number

num = 5

fact = 1

for i in range(1, num + 1):
    fact = fact * i

print("Factorial =", fact)


# 19. Multiplication tables from 1 to 8

for i in range(1, 9):
    print("Table of", i)

    for j in range(1, 11):
        print(i, "x", j, "=", i * j)

    print()


# 20. Print 1 and 2 only

lst = [1, 2, 3, 4]

for i in lst:
    if i == 1 or i == 2:
        print(i)


# 21. Sum of odd numbers in range

total = 0

for i in range(1, 101):
    if i % 2 != 0:
        total += i

print("Sum of odd numbers:", total)


# 22. Sum of even numbers in range

total = 0

for i in range(1, 101):
    if i % 2 == 0:
        total += i

print("Sum of even numbers:", total)


# 23. Count spaces in a string

text = "Python is fun"

count = 0

for i in text:
    if i == " ":
        count += 1

print("Spaces:", count)


# 24. Cube of list elements

lst = [1, 2, 3, 4]

new_list = []

for i in lst:
    new_list.append(i ** 3)

print(new_list)


# 25. Reverse a string

a = "programming"

reverse = ""

for i in a[::-1]:
    reverse += i

print(reverse)


# 26. Print 0 to 7 only using break

for i in range(50):
    if i == 8:
        break
    print(i)


# 27. Print every letter of a string

text = "Python"

for i in text:
    print(i)


# 28. Hello with names only

a = ["ram", "shyam", 1, 2]

for i in a:
    if type(i) == str:
        print("Hello!", i)


# 29. Add Dr. prefix

a = ["ram", "shyam", 1, 2]

new_list = []

for i in a:
    new_list.append("Dr." + str(i))

print(new_list)


# 30. Append square of each number

lst = [1, 2, 3, 4]

new_list = []

for i in lst:
    new_list.append(i ** 2)

print(new_list)


# 31. Append positive numbers only

lst1 = [111, 32, -9, -45, -17, 9, 85, -10]

new_list = []

for i in lst1:
    if i > 0:
        new_list.append(i)

print(new_list)


# 32. Print numbers except 3 and 6

lst = [0, 1, 2, 3, 4, 5, 6]

for i in lst:
    if i == 3 or i == 6:
        continue
    print(i)


# 33. Append types to second list

lst1 = [1, "a", 2.5, True]

lst2 = []

for i in lst1:
    lst2.append(type(i))

print(lst2)


# 34. Use else with for loop

for i in range(5):
    print(i)
else:
    print("Done")


# 35. Series 105 98 ... 7

for i in range(105, 6, -7):
    print(i, end=" ")


# 36. Remove bad characters

bad_chars = [';', ':', '!', "*"]
text = "py;th* o:n ! ;py * t*h:o !n"

result = ""

for i in text:
    if i not in bad_chars and i != " ":
        result += i

print(result)


# 37. Count even and odd numbers

numbers = [1, 2, 3, 4, 5, 6, 7]

even = 0
odd = 0

for i in numbers:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even numbers:", even)
print("Odd numbers:", odd)


# 38. Sum of multiples of 3 or 5 below 100

total = 0

for i in range(3, 100):
    if i % 3 == 0 or i % 5 == 0:
        total += i
print(total)


# 39. Sum of even and odd separately

even_sum = 0
odd_sum = 0
for i in range(1, 101):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i

print("Even Sum:", even_sum)
print("Odd Sum:", odd_sum)


# 40. Count occurrence of a specific number

lst = [1, 2, 3, 2, 4, 2, 5]
search = 2
count = 0
for i in lst:
    if i == search:
        count += 1
print("Count =", count)