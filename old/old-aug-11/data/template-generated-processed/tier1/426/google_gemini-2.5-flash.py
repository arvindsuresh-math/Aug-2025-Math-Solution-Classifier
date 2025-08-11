def solve():
    """Index: 426.
    Returns: the total number of students in both levels.
    """
    # L1
    four_times_multiplier = 4 # four times the number of students
    middle_school_students = 50 # number of students in Middle school is 50
    four_times_middle_school = four_times_multiplier * middle_school_students

    # L2
    less_than_three = 3 # three less than four times
    elementary_school_students = four_times_middle_school - less_than_three

    # L3
    total_students = elementary_school_students + middle_school_students

    # FA
    answer = total_students
    return answer