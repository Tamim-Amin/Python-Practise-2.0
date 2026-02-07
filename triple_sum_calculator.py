# Write a Python program to calculate the sum of three given numbers. If the values are equal, return three times their sum.
number1=float(input("Enter the first number: "))
number2=float(input("Enter the second number: "))
number3=float(input("Enter the third number: "))
if number1==number2==number3:
    print("The sum of three number is : ", number1*3)
else:
    print("The sum of three number is : ",number1+number2+number3)