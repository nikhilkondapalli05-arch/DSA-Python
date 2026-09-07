numbers = [10, 20, 30, 20]
for i in range(len(numbers)):
    for j in range(1 + i,len(numbers)):
        if numbers[i] == numbers[j]:
            print("duplicate : ",numbers[i])