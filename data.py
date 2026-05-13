#question 1
items = [3,5,7,9,11,13]
a=items.pop(4)
items.insert(2,a)
items.append(a)
print(items)

# question 2

first_set: {23,42,65,57,78,83,29}
second_set: {57,83,29,67,73,43,48}
intersection = first_set & second_set
if intersection != {*()}:
    difference = first_set - second_set

