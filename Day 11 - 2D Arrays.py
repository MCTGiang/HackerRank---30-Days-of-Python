# Given a 6x6 2D Array, A:
# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# We define an hourglass in A to be a subset of values with indices falling in this pattern in A's graphical representation:
# a b c
#   d
# e f g
# There are 16 hourglasses in A, and an hourglass sum is the sum of an hourglass' values.
# Task: Calculate the hourglass sum for every hourglass in A, then print the maximum hourglass sum.

!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    # Input: Read the 6x6 array
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    # Def
    def max_hourglass_sum(arr):
        # Initialize the maximum hourglass sum as a very small value
        max_sum = float('-inf')
        # Loop through each possible hourglass starting point
        for i in range(4):  # Rows: 0 to 3
            for j in range(4):  # Columns: 0 to 3
                # Calculate the hourglass sum
                hourglass_sum = (
                    arr[i][j]     + arr[i][j+1]     + arr[i][j+2] +
                                arr[i+1][j+1] +
                    arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
                )
                # Update the maximum hourglass sum if needed
                max_sum = max(max_sum, hourglass_sum)
        return max_sum
    # Output the maximum hourglass sum
    print(max_hourglass_sum(arr))
