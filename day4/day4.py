import unittest

from day4_oop import read_input_numbers, find_answer


class MyTestCase(unittest.TestCase):
    def test_small(self):
        answer = find_answer('test.csv')
        self.assertEqual(answer, 4512)

    def test_input(self):
        answer = find_answer('input.csv')
        self.assertEqual(answer, 72770)

if __name__ == '__main__':
    unittest.main()
