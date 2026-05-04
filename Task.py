number = int(input("enter a number: "))

if number <=100 and number >=1:
    print("the given number is between 1-100")

#Question 2

num = int(input("enter a number: "))

if num%2==0:
    print("number is even")
else:
    print("number is odd")

#Question 3

num = int(input("enter a number"))

if num>=1 and num <=12:
    if num ==1:
        print("January")
    elif num ==2:
        print("February")
    elif num ==3:
        print("March")
    elif num == 4:
        print("April")
    elif num == 5:
        print("May")
    elif num == 6:
        print("june")
    elif num == 7:
        print("july")
    elif num == 8:
        print("august")
    elif num ==9:
        print("september")
    elif num==10:
        print("october")
    elif num==11:
        print("november")
    elif num ==12:
        print("december")
else:
    print("invalid nummber")

#Question 4

marks = int(input("enter marks"))

if marks >= 80:
    print("grade : A")
elif marks >=60 and marks <80:
    print("grade: B")
elif marks >=50 and marks <60:
    print("grade: C")
elif marks >=45 and marks <50:
    print("grade: D")
elif marks >= 25 and marks <45:
    print("grade: E")
elif marks<=25:
    print("grade: F failed")

#Question 5

num = 14

if num%7==0:
    print("number is divisible by 7")

#Question 6

num1 = int(input("enter first number: "))
num2 = int(input("enter second number"))
operator = int(input("enter a operator (+,-,,*,/): "))
if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Cannot divide by zero"
else:
    result = "Invalid operator"

#Question 7

salary = 50000
credit_score = 800
if salary >= 50,000 and credit_score >= 700:
    print("eligible")
else:
    print("not eligible")

#Question 8

num = int(input("enter a number"))
if num%3==0 and num%5==0:
    print("FizzBuzz")
elif num%3==0:
    print("Fizz")
elif num%5==0:
    print("Buzz")
else:
    print(f"{num}")

#Question 9

List = ['a','e','i','o','u']
letter = input("enetr a letter").lower()
if letter in list:
    print(f"{letter} is a vowel")
else:
    print("letter is not a vowel")

#Question 10

marks = input("enter the marks")
if marks >=10 and marks <=100:
    print("A")
elif marks >=89  and  marks <=80:
    print("B")
elif marks >=79 and marks <=70:
    print("C")
else:
    print("fail")

#Question 11

age = int(input("enter age"))
if age < 13:
    print("child")
elif age >= 13 and age <=19:
    print("teenager")
else:
    print("adult")

#Quetsion 12

python = "SAN"
if python.isupper():
    print("upper case")
elif python.isdigit():
    print("digit")
elif python.islower():
    print("lower case")
else:
    print("special character")

#Question 13

color = input("Enter a color (Red, Yellow, Green): ")

if color.lower() == "red":
    print("Stop")
elif color.lower() == "yellow":
    print("Get Ready")
elif color.lower() == "green":
    print("Go")
else:
    print("Invalid color")

#Question 14

age = int(input("Enter your age: "))
experience = int(input("Enter your years of experience: "))

if age > 18 and experience >= 2:
    print("Eligible")
else:
    print("Not Eligible")

#Question 15

temp = float(input("Enter the temperature in °C: "))

if temp > 30:
    print("It's hot, stay hydrated!")
elif 15 <= temp <= 30:
    print("Enjoy the weather!")
else:
    print("It's cold, wear warm clothes!")

#Question 16

menu = input("enter a food item(pizza, burger, pasta): ")
if menu == "pizza":
    print("price = $10")
elif menu == "burger":
    print("price = $7")
elif menu == "pasta":
    print("price = $8")
else:
    print("invalid menu item")

#Question 17

height = int(input("enter your height"))
if height >=6:
    print("selected")
else:
    print("not selected")

#Question 18

age = int(input("enter a number"))
if age >= 18:
    print("allowed")
else:
    print("not allowed")

#Quetsion 19

username = "admim"
password = "password123"

entered_user = "admin"
entered_pass = "123"

if entered_user == username and entered_pass == password:
    print("access granted")
else:
    print("acces denied")

#Question 20

month = int(input("Enter month number (1-12): "))

if month in [12, 1, 2]:
    print("Winter")
elif month in [3, 4, 5]:
    print("Spring")
elif month in [6, 7, 8]:
    print("Summer")
elif month in [9, 10, 11]:
    print("Autumn")
else:
    print("Invalid month number")


            





 
