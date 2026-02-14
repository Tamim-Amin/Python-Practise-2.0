# Write a Python program to create a histogram from a given list of integers.
def histogram(numbers):
    if not numbers:
        return "Empty list"
    for num in numbers:
        print(f"{num} | {'*' * num}")

number=list(map(int,input("Enter any integer number separate by comma: ").split(",")))
histogram(number)