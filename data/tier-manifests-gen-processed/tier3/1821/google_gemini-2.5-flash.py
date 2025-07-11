def solve():
    """Index: 1821.
    Returns: the number of students who have not yet had their picture taken.
    """
    # L1
    total_students = 24 # 24 students in the class
    fraction_denominator_before_lunch = 3 # One-third had their school portraits taken
    students_photographed_before_lunch = total_students / fraction_denominator_before_lunch

    # L2
    additional_students_after_lunch = 10 # 10 additional students had their portraits taken
    total_photographed_by_gym_class = students_photographed_before_lunch + additional_students_after_lunch

    # L3
    students_remaining = total_students - total_photographed_by_gym_class

    # FA
    answer = students_remaining
    return answer