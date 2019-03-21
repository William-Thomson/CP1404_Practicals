"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur? When the numerator or denominator isn't an int.
2. When will a ZeroDivisionError occur? during the fraction execution
3. Could you change the code to avoid the possibility of a ZeroDivisionError? Error check so a number not 0 must be entered.
"""

# try:
#     numerator = int(input("Enter the numerator: "))
#     denominator = int(input("Enter the denominator: "))
#     while denominator == 0:
#         denominator = int(input("Denominator cannot be 0. Enter denominator: "))
#     fraction = numerator / denominator
#     print(fraction)
# except ValueError:
#     print("Numerator and denominator must be valid numbers!")
# print("Finished.")


"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

finished = False
result = 0
while not finished:
    try:
        result = int(input("Enter number: "))
        finished = True
        pass
    except ValueError:
        print("Please enter a valid integer.")
print("Valid result is:", result)
