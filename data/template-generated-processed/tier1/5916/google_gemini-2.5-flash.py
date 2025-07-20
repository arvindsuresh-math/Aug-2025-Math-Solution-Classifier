def solve():
    """Index: 5916.
    Returns: the total number of students in the class.
    """
    # L1
    female_students = 13 # 13 female students
    male_multiplier = 3 # three times as many male students
    male_students = female_students * male_multiplier

    # L2
    total_students = male_students + female_students

    # FA
    answer = total_students
    return answer