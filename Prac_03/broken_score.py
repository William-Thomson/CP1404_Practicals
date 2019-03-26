"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


def main():
    score = float(input("Enter score: "))
    print(grade(score))


def grade(score):
    if score < 0 or score > 100:
        grade_name = "Invalid score"
    elif score >= 90:
        grade_name = "Excellent"
    elif score >= 50:
        grade_name = "Passable"
    else:
        grade_name = "Bad"
    return grade_name


main()
