def find_kth_largest(arr, k):
    if len(arr) < k:
        raise ValueError("Розмір масиву менший за k.")
    sorted_arr = sorted(arr, reverse=True)
    kth_value = sorted_arr[k - 1]
    index_in_original = arr.index(kth_value)
    return kth_value, index_in_original

if __name__ == "__main__":
    arr = [15, 7, 22, 9, 36, 2, 42, 18]
    k = 3
    value, index = find_kth_largest(arr, k)
    print(f"{k}-й найбільший елемент: {value} ")
    print(f"його позиція в масиві: {index}")

import unittest

class TestFindKthLargest(unittest.TestCase):
     def test_basic_case(self):
        arr = [15, 7, 22, 9, 36, 2, 42, 18]
        value, index = find_kth_largest(arr, 3)
        self.assertEqual(value, 22)
        self.assertEqual(index, 2)
    
     def test_first_largest(self):
        arr = [ 4, 10, 1]
        value, index = find_kth_largest(arr, 1)
        self.assertEqual(value, 10)
        self.assertEqual(index, 1)
     
     def test_invalid_k(self):
        with self.assertRaises(ValueError):
            find_kth_largest([1, 2], 5)
        
if __name__ == "__main__":
    unittest.main()

    
        
        




