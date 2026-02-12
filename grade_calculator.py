"""
Grade Calculator Module
Provides functions for calculating grades, finding highest/lowest scores, and assigning letter grades.
"""


def calculate_average(grades):
    """
    Calculate the average of a list of grades.
    """

    if len(grades) == 0:
        return 0
    return sum(grades) / len(grades)


def find_highest(grades):
    """
    Find the highest grade in a list of grades.
    """

    if len(grades) == 0:
        return None
    return max(grades)


def find_lowest(grades):
    """
    Find the lowest grade in a list of grades.
    """
    if len(grades) == 0:
        return None
    return min(grades)


def assign_letter_grade(average):
    """
    Convert a numeric average to a letter grade.
    """
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"