### This is an unthinkably horrible hack to allow
### Python unit tests to work better in zyLabs.
### This must be done before importing unittest.
### DO NOT CHANGE THESE NEXT TWO LINES
import sys

import unittest.test
sys.stderr = sys.stdout
### DO NOT CHANGE THE PREVIOUS TWO LINES

import unittest

from list_utils import *

class TestFind(unittest.TestCase):

    def setUp(self):
        self.collatz_array = [27, 82, 41, 124]

    def test_successful_find(self):
        for i in range(len(self.collatz_array)):
            self.assertEqual(find(self.collatz_array, self.collatz_array[i]), i)

    def test_failed_find(self):
        self.assertIsNone(find(self.collatz_array, 42))

class TestCount(unittest.TestCase):

    def setUp(self):
        self.all_ones = [1,1,1,1,1,1]
        self.collatz_array = [27, 82, 41, 124, 62, 31, 94]

    def test_all_equal(self):
        self.assertEqual(count(self.all_ones, 1), 6)
        self.assertEqual(count(self.all_ones, 0), 0)

    def test_all_different(self):
        for i in range(len(self.collatz_array)):
            self.assertEqual(count(self.collatz_array, self.collatz_array[i]), 1)

class TestMinElement(unittest.TestCase):
    pass

class TestMaxElement(unittest.TestCase):
    pass

if __name__ == "__main__":
    unittest.main()
