alpha=input("Enter any alphabet: ").lower()
vowels=["a","e","i","o","u"]
if alpha in vowels:
    print(f"{alpha} is a vowel.")
else:
    print(f"{alpha} is a consonant.")