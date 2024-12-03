# Given an array, A, of N integers, print A's elements in reverse order as a single line of space-separated numbers.
# Example
# A = [1,2,3,4]
# Print 4 3 2 1. 
# Each integer is separated by one space.

#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    # Read the size of the array
    n = int(input())
    # Read the array elements
    arr = list(map(int, input().split()))
    # Reverse the array
    reversed_arr = reversed(arr)
    # Print the reversed array as a single line of space-separated numbers
    print(" ".join(map(str, reversed_arr)))
