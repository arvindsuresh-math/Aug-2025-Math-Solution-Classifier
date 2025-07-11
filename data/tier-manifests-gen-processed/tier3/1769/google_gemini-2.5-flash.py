def solve():
    """Index: 1769.
    Returns: the number of students who like yellow best.
    """
    # L1
    total_students = 30 # class of 30 students
    green_fraction_denominator = 2 # Half of the class
    green_students = total_students / green_fraction_denominator

    # L2
    total_girls = 18 # If there are 18 girls in the class
    pink_fraction_denominator = 3 # one-third of the girls
    pink_girls = total_girls / pink_fraction_denominator

    # L3
    green_or_pink_students = green_students + pink_girls

    # L4
    yellow_students = total_students - green_or_pink_students

    # FA
    answer = yellow_students
    return answer