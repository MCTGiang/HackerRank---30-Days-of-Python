# Function Description
# Complete the factorial function in the editor below. Be sure to use recursion.
# factorial has the following paramter:
# •	int n: an integer
# Returns
# •	int: the factorial of 
# Note: If you fail to use recursion or fail to name your recursive function factorial or Factorial, you will get a score of 0.
# Input Format
# A single integer,  (the argument to pass to factorial).
# Constraints
# •	2 =< n =< 12
# •	Your submission must contain a recursive function named factorial.

#!/bin/python3

import math
import os
import random
import re
import sys

# Definition factiorial function
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * (factorial(n-1))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = factorial(n)

    fptr.write(str(result) + '\n')

    fptr.close()
