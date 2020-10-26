# Authored by elia on 22/10/2020 

# Feature: #Enter feature name here
# Enter feature description here

# Scenario: # Enter scenario name here
"""

"""

from unittest import TestCase
from src.main.util.binary_ops import *

class TestBinaryOps(TestCase):
    def test_binary_str_to_int(self):
        self.assertEqual(int('11111111',2), 255)
        # self.assertEqual(binary_str_to_int('11111111'), 255)

    def test_digit_count_to_binary_str(self):
        self.assertEqual(digit_count_to_binary_str(377373737), '11111111')
        self.assertEqual(digit_count_to_binary_str(3), '111')

    def test_get_max_number_for_binary_digit_count(self):
        self.assertEqual(get_max_number(3) ,7)
        self.assertEqual(get_max_number(4), 15)

    def test_get_bin_str_with_max_count(self):
        self.assertEqual(len(get_bin_str_with_max_count(2446324111, 33)), 33)
