# Write a Python program to calculate the difference between a given number and 17. 
# If the number is greater than 17, return twice the absolute difference.
number=float(input("Enter a number: "))
difference=number-17
if number>17:
    print("The difference is twice the absolute value:", 2 * abs(difference))
else:
    print("The difference is:",difference)