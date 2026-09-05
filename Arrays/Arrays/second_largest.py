print("Finding second highest number in list")

numbers = [10, 25, 7, 40, 15, 30]

maximum = 0
second_maximum = 0

for i in numbers:
    if i > maximum:
        second_maximum = maximum
        maximum = i
    elif i > second_maximum:
        second_maximum = i

print(second_maximum)
