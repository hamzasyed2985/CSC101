size = int(input("Enter size of array: "))
num = []
for i in range(size):
    next_num = int(input("Enter the next number: "))
    num.append(next_num)

count = 1
for i in range(size):
    if i < size - 1 and num[i] == num[i + 1]:
        count += 1
    else:
        count = 1

print(count)