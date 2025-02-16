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

class TestFindMaxMin(unittest.TestCase):

    def test_basic(self):
        numbers = [3, 9, 2, 8, 1]
        result = find_max_min(numbers)
        print("Array:", numbers, "-> Result:", result)
        self.assertEqual(result, (9, 1))

    def test_single_element(self):
        numbers = [5]
        result = find_max_min(numbers)
        print("Array:", numbers, "-> Result:", result)
        self.assertEqual(result, (5, 5))

    def test_all_equal(self):
        numbers = [4, 4, 4, 4]
        result = find_max_min(numbers)
        print("Array:", numbers, "-> Result:", result)
        self.assertEqual(result, (4, 4))

    def test_negative_numbers(self):
        numbers = [-3, -1, -7, -2]
        result = find_max_min(numbers)
        print("Array:", numbers, "-> Result:", result)
        self.assertEqual(result, (-1, -7))

    def test_mixed_numbers(self):
        numbers = [0, -10, 10, 5, -5]
        result = find_max_min(numbers)
        print("Array:", numbers, "-> Result:", result)
        self.assertEqual(result, (10, -10))

if __name__ == '__main__':
    unittest.main(verbosity=2)
