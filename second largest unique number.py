def second_largest_unique(numbers):
    unique_values = set(numbers)

    if len(unique_values) < 2:
        return -1
      
    first = second = float('-inf')
    for num in unique_values:
        if num > first:
            second = first
            first = num
        elif num > second:
            second = num

    return second

print(second_largest_unique([3, 5, 2, 5, 6, 6, 1])) 
print(second_largest_unique([7, 7, 7]))             
print(second_largest_unique([10, 9, 8, 8]))         
