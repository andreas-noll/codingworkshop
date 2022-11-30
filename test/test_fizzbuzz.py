"""Test module for fizzbuzz"""

import unittest

from workshop.fizzbuzz import fizzbuzz


class TestCases(unittest.TestCase):
    """Class for test cases"""

    def test_fizzbuzz__zero__empty_string(self):
        output = fizzbuzz(0)
        self.assertEqual("", output)

    def test_fizzbuzz__one__fizz(self):
        output = fizzbuzz(1)
        self.assertEqual("fizz", output)

    def test_fizzbuzz__one_two_four_five__string_of_len_input_times_4(self):
        inputs = [1, 2, 4, 5]
        outputs = []
        for input in inputs:
            outputs.append(len(fizzbuzz(input)))
        self.assertListEqual([4, 8, 16, 20], outputs)

    def test_fizzbuzz__two__fizzbuzz(self):
        input = 2
        output = fizzbuzz(input)
        self.assertEqual("fizzbuzz", output)
