import unittest
from arithmetic import subtract, add, mult, find_duplicates_in_set

class TestArithmetic(unittest.TestCase):
    def test_add(self):
        result = add(10, 12)
        self.assertEqual(result, 22)

    def test_subtract(self):
        result = subtract(10,2)
        self.assertEqual(result,8)

    def test_mult(self):
        result = mult(2,10)
        self.assertEqual(result, 20)

    def test_find_duplicates_in_set(self):
        result = find_duplicates_in_set([1,2,3,4,5,5,6])
        self.assertEqual(result ,[5])

if __name__ == '__main__':
    unittest.main()