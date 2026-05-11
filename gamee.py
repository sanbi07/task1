'''print("WELCOME TO THE MAGIC FOREST")
direct = input("go north or south, select your direction: ").lower()
if direct == "north":
    chose = input("cross the river or follow the path: ").lower()
    if chose == "cross the river":
        character = input("choose fairy, ogre, or elf: ").lower()
        if character =="elf":
            print("you WIN!")
        else:
            print("LOOSER BOOOOOO")
    else:
        print("LOOSER BOOOOO")
else:
    print("LOOSER BOOOOOOOOO") '''


'''height = float(input("enter your height in cm: "))
weight = float(input("enter your weight in kg: "))
bmi = weight/height**2
if bmi < 18.5:
    print("you are underweight")
elif bmi >= 18.5 and bmi <=25:
    print("normal weight")
elif bmi >=25 and bmi <=30:
    print("overweight")
else:
    print("obese")
print (f"weight: {weight}")
print(f"height: {height}")
print(f"BMI: {bmi}")
'''

username = "admin"
password = "add123"

entered_user = input("enter a username: ")
entered_password = input("enter your password: ")
if entered_user == username:
    if entered_password == password:
        print("valid login")
    else:
        print("password is incorrect")
else:
    print("username is invalid")

#question 18
num = int(input("enter a number: "))
if num < 0:
    if num%2==0:
        print("number is even")
    else:
        print("number is odd")





