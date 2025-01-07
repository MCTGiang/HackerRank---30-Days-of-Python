# Given a base- 10 integer, n, convert it to binary (base-21).
# Then find and print the base-10 integer denoting the maximum number of consecutive 1's in n's binary representation.
# When working with different bases, it is common to show the base as a subscript.

!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
    def max_consecutive_ones(n):
        if not (1 <= n <= 10**6):
            raise ValueError("Input must be a non-negative integer.") 
        # Convert the number to binary
        binary_representation = bin(n)[2:]
        # Split the binary representation by '0' to find groups of '1's
        consecutive_ones = binary_representation.split('0')
        # Find the length of the longest group of '1's
        max_ones = max(len(group) for group in consecutive_ones)
        return max_ones
    # Output
    print(max_consecutive_ones(n))
