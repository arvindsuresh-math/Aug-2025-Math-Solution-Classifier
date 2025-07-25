def solve():
    """Index: 2364.
    Returns: the lowest grade the absent student can get for the class to still get a pizza party.
    """
    # L1
    num_students = 25 # 25 students in the class
    required_average = 0.75 # average score on their quiz is higher than 75%
    total_required_percentage = num_students * required_average

    # L2
    students_present = 24 # One student is absent
    present_average = 0.77 # average score of the students who took the test was 77%
    total_present_percentage = students_present * present_average

    # L3
    percent_factor = 100 # WK
    lowest_absent_grade = (total_required_percentage - total_present_percentage) * percent_factor

    # FA
    answer = lowest_absent_grade
    return answer