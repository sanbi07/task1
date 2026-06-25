#Qno:3 
def add(num1,num2):
    return num1 + num2
def substract(num1,num2):
    return num1 - num2
def multiply(num1,num2):
    return num1 * num2
def divide (num1,num2):
    if num2==0:
        return "Error: Division by zero is not allowed."
    return num1 / num2
def calculator():
    while True:
        print ("/n---simple calculator---")
        print("1. Add")
        print("2. Substarct")
        print("3. multiply")
        print("4. divide")
        print("5. Exit")
        choice = input("Select an option (1-5): ")
        if choice == '5':
            print("Exiting calculator. Goodbye!")
            break
        num1 = int(input("Enter your first number : "))
        num2 = int(input("Enter your second number: "))
        if choice==1:
            print("Add is", add(num1,num2))
        if choice==2:
            print("Substract is", substract(num1,num2))
        if choice==3:
            print("multipy is", multiply(num1,num2))
        if choice==4:
            print("divide is", divide(num1,num2))
        else:
            print("invalid choice")
calculator()

#Qno-4

def remove_at_idx(lst, idx):
    new_list = lst.copy()
    if 0 <= idx < len(new_list):
        new_list.pop(idx)
    return new_list
numbers = [10, 20, 30, 40, 50]
print(remove_at_idx(numbers, 2))

#Qno-5

def square_list():
    lst = []
    for i in range(1, 21):
        lst.append(i ** 2)
    print(lst[:5])
square_list()

#Qno=6
course = [{'title': 'AncientCivilizations', 'genre': 'history'}, 
          {'title': 'Corporate Finance', 'genre': 'commerce'}, 
          {'title':'Modern World History', 'genre': 'history'} ]
result = filter(lambda x: x ['genre']=='history,course')
for i in course:
    print(i['title'])

#Qno=7

emails = ['ram.sharma@gmail.com', 'spam@hooya.com', 'virus@malware.net','shyam.kumar@workcorp.com']
blacklist = ('@hooya.com', '@malware.net')
result = filter(lambda x : x.endswith(blacklist),emails)
print(list(result))

#Qno-8



price= [100, 50, 200, 75]
discount =0.8
result = filter(lambda x : x*discount,price)
print(list(result))



