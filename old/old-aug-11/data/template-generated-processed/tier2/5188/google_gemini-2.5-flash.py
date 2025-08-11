def solve():
    """Index: 5188.
    Returns: the number of students who do not have glasses.
    """
    # L1
    total_percentage = 100 # WK
    percentage_with_glasses = 40 # 40 percent of the students have glasses
    percentage_without_glasses = total_percentage - percentage_with_glasses

    # L2
    total_students = 325 # 325 students in a local high school
    decimal_for_ten_percent = 0.10 # WK
    value_of_ten_percent_students = total_students * decimal_for_ten_percent

    # L3
    multiplier_for_sixty_percent = 6 # WK
    students_without_glasses = value_of_ten_percent_students * multiplier_for_sixty_percent

    # FA
    answer = students_without_glasses
    return answer