numbers = [10, 20, 30, 20, 40, 30]
found = False
for i in range(len(numbers)):
    for j in range(1 + i,len(numbers)):
        if numbers[i] == numbers[j]:
            print(numbers[i])
            found = True
            break
    if found:
        break


