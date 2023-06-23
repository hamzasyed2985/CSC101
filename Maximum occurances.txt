def find_max_occurrences(array):
    occurrences = {}
    max_count = 0

    for num in array:
        if num in occurrences:
            occurrences[num] += 1
        else:
            occurrences[num] = 1

        if occurrences[num] > max_count:
            max_count = occurrences[num]

    max_numbers = [num for num, count in occurrences.items() if count == max_count]
    return max_numbers, max_count

# Example usage
arr = [1, 2, 3, 2, 4, 1, 2, 2, 3, 3, 3]
max_numbers, max_count = find_max_occurrences(arr)
print("Number(s) with maximum occurrences:", max_numbers)
print("Maximum count:", max_count)