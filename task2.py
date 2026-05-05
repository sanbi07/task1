#Question 1
age = int(input("enter your age : "))
height = int(input("enter your height"))
if age>=12 and height>=140:
    print("you can ride the roller coaster")
else:
    print("you cannot ride the roller coaster")

#Question 2
color = input("Enter a color (Red, Yellow, Green): ")

if color.lower() == "red":
    print("Stop")
elif color.lower() == "yellow":
    print("Get Ready")
elif color.lower() == "green":
    print("Go")
else:
    print("Invalid color")

#Question 3
num = {1:'spring',2:'summer',3:'autum',4:'winter'}

p = int(input("enter a number "))
if p in num:
    print(num[p])
else:
    print("enter a valid number: ")

#solve by match case
number = int(input("enter a number between 1 to 4: "))
match number:
    case 1:
        print("spring")
    case 2:
        print("summer")
    case 3:
        print("autum")
    case 4:
        print("winter")
    case _:
        print("invalid input")

#Question 4
username = "admin"
password = "pass123"

entered_user = input("enter a username: ")
entered_password = input("enter your password: ")
if entered_user == username:
    if entered_password == password:
        print("valid login")
    else:
        print("password is incorrect")
else:
    print("username is invalid")

#Quesion 5
age = int(input("enter your age"))
income = int(input("enter your income"))
credit = int(input("enter credit score"))
if age>= 21 and age <=60:
    if income>=30000:
        if credit>=700:
            print("loan approved")
        else:
            print("failed credit score")
    else:
        print("failed income")
else:
    print("age requirement does not meet")

#Question 6
age = int(input("enter your age"))
membership = input("do you have a memebership (yes/no): ").lower()

if age<12:
    print("your ticket is free")
else:
    if membership =='yes':
        if age >= 60:
            print("you get a senior citizen discount total is 100")
        else:
            print("the ticket price is 150")

#Question 7
salary = float(input("enter your salary: "))
years = int(input("enter your years of service: "))

if years > 5:
    bonus = salary * 0.05
    print("bonus amount: Rs.",bonus)
else:
    print("no bonus")

#Question 8
import math
radius = float(input("Enter the radius of the circle: "))
area = math.pi * radius ** 2
print("The area of the circle is:", area)

#Question 9
age = int(input("enter your age"))
gender = input("enter gender (M/F): ").upper()
days = int(input("enter days: "))

if age >=18 and age<30:
    if gender == 'M':
        wage = 700
    elif gender == 'F':
        wage = 750
elif age >=30 and age <= 40:
    if gender == 'M':
        wage = 800
    elif gender == 'F':
        wage = 850

if wage > 0:
    total = wage * days
    print(f"total wages: {total}")
else:
    print("criteria not met")

#Question 10

num = int(input("enter a number"))
if num%3==0 and num%5==0:
    print("fizz buzz")
elif num %3==0:
    print("fizz")
elif num%5==0:
    print("buzz")
else:
    print(num)            






