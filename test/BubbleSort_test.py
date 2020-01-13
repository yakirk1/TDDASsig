import unittest

from src.BubbleSort import BubbleSort


class BubbleSort_test(unittest.TestCase):
<<<<<<< HEAD
    def test_something(self):
        self.as000000000sertEqual(True, False)
=======
    def test_sort_correct(self):
        # stub
        arr1 = (1, 3, 2, 0)
        arr2 = [1, 2, 3, 4]
        arr3 = [-5, -10, -8, -4]
        arr4 = ['ca', 'av', 'B', 'cb']
        arr5 = ['2', 'z', '@', 'h']
        arr6 = map(lambda x: x * x, [1, 3, 2])
        arr7 = filter(lambda x: x % 2 == 0, (4, 3, 0, 1, 2))
        arr8 = [2, 2, 2, 2]
        arr9 = []
        arr10 = [-5, 2, -5, 3, 2]
        arr11 = 3
        arr12 = '#'

        # assume
        expected1 = [0, 1, 2, 3]
        expected2 = [1, 2, 3, 4]
        expected3 = [-10, -8, -5, -4]
        expected4 = ['B', 'av', 'ca', 'cb']
        expected5 = ['2', '@', 'h', 'z']
        expected6 = [1, 4, 9]
        expected7 = [0, 2, 4]
        expected8 = [2, 2, 2, 2]
        expected9 = []
        expected10 = [-5, -5, 2, 2, 3]
        expected11 = 3
        expected12 = '#'

        # action
        result1 = BubbleSort.sort(arr1)
        result2 = BubbleSort.sort(arr2)
        result3 = BubbleSort.sort(arr3)
        result4 = BubbleSort.sort(arr4)
        result5 = BubbleSort.sort(arr5)
        result6 = BubbleSort.sort(arr6)
        result7 = BubbleSort.sort(arr7)
        result8 = BubbleSort.sort(arr8)
        result9 = BubbleSort.sort(arr9)
        result10 = BubbleSort.sort(arr10)
        result11 = BubbleSort.sort(arr11)
        result12 = BubbleSort.sort(arr12)

        # expect/assert
        self.assertEqual(result1, expected1)
        self.assertEqual(result2, expected2)
        self.assertEqual(result3, expected3)
        self.assertEqual(result4, expected4)
        self.assertEqual(result5, expected5)
        self.assertEqual(result6, expected6)
        self.assertEqual(result7, expected7)
        self.assertEqual(result8, expected8)
        self.assertEqual(result9, expected9)
        self.assertEqual(result10, expected10)
        self.assertEqual(result11, expected11)
        self.assertEqual(result12, expected12)

    def test_invalid_types(self):
        # stub
        arr1 = ['a', 1, 'c', 'b']
        arr2 = [2, 'a', True, 'h']
        arr3 = lambda x: x + x

        # assume
        expected = TypeError

        # action
        result1 = BubbleSort.sort(arr1)
        result2 = BubbleSort.sort(arr2)
        result3 = BubbleSort.sort(arr3)

        # expect/assert
        self.assertRaises(expected, result1)
        self.assertRaises(expected, result2)
        self.assertRaises(expected, result3)

    def test_valid_length(self):
        # stub
        arr1 = ['abc', 'adc', 'ada']
        arr2 = (6, 2, 5, 4, 1)
        arr3 = map(lambda x: x.upper(), ['a', 'd', 'c', 'b'])

        # assume
        expected1 = 3
        expected2 = 5
        expected3 = 4

        # action
        result1 = len(BubbleSort.sort(arr1))
        result2 = len(BubbleSort.sort(arr2))
        result3 = len(BubbleSort.sort(arr3))

        # expect/assert
        self.assertEqual(expected1, result1)
        self.assertEqual(expected2, result2)
        self.assertEqual(expected3, result3)
>>>>>>> f1bd447aa7803b56b6e247ac92facdb40c3f6db9


if __name__ == '__main__':
    unittest.main()
