#Task: Given a string, S, of length N that is indexed from 0 to N-1, print its even-indexed and odd-indexed characters as 2 space-separated strings on a single line (see the Sample below for more detail).
# Note: 0 is considered to be an even index.

# Input Format
# The first line contains an integer, T (the number of test cases).
# Each line i of T the  subsequent lines contain a string, S.
# Constraints
# •	1 <= T <=10
# •	2 <= length of S  <= 10000
# Output Format
# For each String Sj (where 1<= j <= T-1), print 's Sj even-indexed characters, followed by a space, followed by Sj's odd-indexed characters.

# Read input from STDIN. Print output to STDOUT
import sys
input = sys.stdin.read  # Read all input from STDIN
# def the calculation
def print_index(s):
    # Split the input into lines
    lines = s.splitlines()
    n = int(lines[0])  # First line contains the number of test cases
    results = []
    
    # Process each test case
    for i in range(1, n + 1):
        line = lines[i]
        even = ""
        odd = ""
        for j in range(len(line)):
            if j % 2 == 0:
                even += line[j]
            else:
                odd += line[j]
        results.append(even + " " + odd)  # Combine even and odd characters
    
    print("\n".join(results))

# Take multiline input
s = str(input())
print_index(s)
