"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


def main():

    score = float(input("Enter score: "))
    result = calculate_score(score)
    print(result)


def calculate_score(score):
    if score < 0 or score > 100:
        result = "Invalid Score"
    elif score >= 90:
        result = "Excellent"
    elif score >= 50:
        result = "Passable"
    elif score < 50:
        result = "Bad"
    else:
        pass
    return result


main()
