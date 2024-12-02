# Given an integer, , perform the following conditional actions:
# If  is odd, print Weird
# If  is even and in the inclusive range of  to , print Not Weird
# If  is even and in the inclusive range of  to , print Weird
# If  is even and greater than , print Not Weird
# Complete the stub code provided in your editor to print whether or not  is weird.

# ensures that the code block inside it will only execute if the script is run directly (not imported as a module)
if __name__ == '__main__':
    # converts the stripped string input into an integer and ssigned to the variable n
    n = int(input().strip())
# Check n is odd
if n % 2 != 0:
    print('Weird')
else:
    # Check n is even and in the inclusive range of 2-5
    if 2 <= n <= 5:
        print('Not Weird')
    # Check n is even and in the inclusive range of 6-20
    elif 6 <= n <= 20:
        print('Weird')
    # Check n is even and greater than 20
    else:
        print('Not Weird')
