# Write a Python program that concatenates all elements in a list into a string and returns it.
def concatenate_lists(listNumber):
    if not listNumber:
        return "Empty list"
    result=""
    for numbers in listNumber:
        result+=str(numbers)
    return result
listNumber=input("Enter any integer number separate by comma: ").split(",")
print(concatenate_lists(listNumber))