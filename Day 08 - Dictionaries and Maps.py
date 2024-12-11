# Given n names and phone numbers, assemble a phone book that maps friends' names to their respective phone numbers. You will then be given an unknown number of names to query your phone book for. For each name queried, print the associated entry from your phone book on a new line in the form name=phoneNumber; if an entry for name is not found, print Not found instead.
# Note: Your phone book should be a Dictionary/Map/HashMap data structure.
# Input Format
# The first line contains an integer, n, denoting the number of entries in the phone book.
# Each of the n subsequent lines describes an entry in the form of 2 space-separated values on a single line. The first value is a friend's name, and the second value is an 8-digit phone number.
# After the n lines of phone book entries, there are an unknown number of lines of queries. Each line (query) contains a name to look up, and you must continue reading lines until there is no more input.
# Note: Names consist of lowercase English alphabetic letters and are first names only.
# Constraints
# •	1 <= n <= 10^5
# •	1 <= queries <= 10^5
# Output Format
# On a new line for each query, print Not found if the name has no corresponding entry in the phone book; otherwise, print the full name and phone Number in the format name=phoneNumber

# Read input from STDIN. Print output to STDOUT
import sys

# def the caculation:
def print_phone(s):
    # Split into key-value pairs by lines
    lines = s.splitlines()
    # First line contains the number of entries in the phone book
    n = int(lines[0]) 
    # Build the phone book dictionary
    phone_book = {}
    for i in range(1, n + 1):
        # Split into key, value
        key, value = lines[i].split(" ")
        # Add to the dictionary
        phone_book[key] = value
    # Process queries
    for query in lines[n+1:]:
        if query in phone_book:
            print(f"{query}={phone_book[query]}")
        else:
            print("Not found")
# Read all input from STDIN
s = sys.stdin.read()
print_phone(s)
