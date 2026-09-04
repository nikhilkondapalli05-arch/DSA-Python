numbers = [10, -5, 20, -8, 0, 15, -3]

positive_count = 0
negative_count = 0

for number in numbers:
    if number > 0:
        positive_count += 1
    if number < 0:
        negative_count += 1

print("Positive numbers:", positive_count)
print("Negative numbers:", negative_count)
