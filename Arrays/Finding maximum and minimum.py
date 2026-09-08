numbers = [12, 5, 28, 3, 19, 40, 7]
maximum = numbers[0]
minimum = numbers[0]
for i in numbers:
    if i > maximum:
        maximum = i
    if i < minimum:
        minimum = i
print("largest : ",maximum)
print("smallest : ",minimum)