# Task: Complete the code in the editor below. The variables , , and  are already declared and initialized for you. You must:
# Declare  variables: one of type int, one of type double, and one of type String.
# Read  lines of input from stdin (according to the sequence given in the Input Format section below) and initialize your  variables.
# Use the  operator to perform the following operations:
# Print the sum of  plus your int variable on a new line.
# Print the sum of  plus your double variable to a scale of one decimal place on a new line.
# Concatenate  with the string you read as input and print the result on a new line.

i = 4
d = 4.0
s = 'HackerRank '
# Declare second integer, double, and String variables.
int_var = 4
float_var = 4.0
string_var = "HackerRank "
# Read and save an integer, double, and String to your variables.
i = int(input())
d = float(input())
s = input()
# Print the sum of both integer variables on a new line.
print(i + int_var)
# Print the sum of the double variables on a new line.
print(f"{d + float_var:.1f}")
# Concatenate and print the String variables on a new line
# The 's' variable above should be printed first.
print(string_var + s)
