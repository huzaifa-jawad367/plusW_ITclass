import unittest

def find_max_min(lst):
    max_val = lst[0]
    min_val = lst[0]

    for num in lst:
        if num > max_val:
            max_val = num
        if num < min_val:
            min_val = num
    
    return max_val, min_val

numbers = [3, 9, 2, 8, 1]
max_val, min_val = find_max_min(numbers)
print(f'Max: {max_val}, Min: {min_val}')