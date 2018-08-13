"""
Q1. When will a ValueError occur?
A1. When a string is entered, not an interger.
Q2. When will a ZeroDivisionError?
A2. When a zero is entered as the denominator.
Q3. Could you change the code to avoid the possibility of a ZeroDivisionError?
A3. Yes, by using a while loop to enter a valid number.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")