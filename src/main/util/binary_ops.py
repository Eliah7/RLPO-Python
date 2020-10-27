# Authored by elia on 22/10/2020 

# Feature: #Enter feature name here
# Enter feature description here

# Scenario: # Enter scenario name here
"""

"""
import numpy as np
import matplotlib.pyplot as plt

def binary_str_to_int(bin_str):
    return int(bin_str, 2)

def digit_count_to_binary_str(count):
    print(count)
    return str(np.ones(count, dtype=np.int))[1:-1].replace(" ", "")


def get_max_number(count):
    return int(digit_count_to_binary_str(count), 2)

def get_bin_str_with_max_count(action, count):
    bin_str = bin(action)[2:]

    remaining_len = count - len(bin_str)
    if remaining_len > 0:
       for i in range(remaining_len):
           bin_str = "0" + bin_str
       return bin_str
    else:
        return bin_str


