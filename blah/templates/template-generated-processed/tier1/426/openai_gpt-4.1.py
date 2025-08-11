def solve():
    """Index: 426.
    Returns: the total number of students in both Elementary and Middle School.
    """
    # L1
    middle_school_students = 50 # number of students in Middle school is 50
    multiplier = 4 # four times the number of students in Middle School
    four_times_middle = multiplier * middle_school_students

    # L2
    less_than = 3 # three less than four times the number in middle school
    elementary_school_students = four_times_middle - less_than

    # L3
    total_students = elementary_school_students + middle_school_students

    # FA
    answer = total_students
    return answer