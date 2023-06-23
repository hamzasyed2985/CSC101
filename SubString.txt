def longest(roll):
    i = 0
    M = 0
    while 0 <= i < len(roll):
        c = 1
        for j in range(i+1, len(roll)):
            if roll[j] != roll[i]:
                i = j
                break
            c += 1
            i += 1
        if c > M:
            M = c
        if i == len(roll) - 1:
            break
    return M

a=input('enter ')
print(longest(a))