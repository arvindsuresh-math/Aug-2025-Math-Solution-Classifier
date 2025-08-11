def solve():
    """Index: 1248.
    Returns: the number of students in Mr. Johnson's class.
    """
    # L1
    finley_class_students = 24 # Mrs. Finley's class has 24 students
    half_divisor = 2 # Half the number
    half_finley_class = finley_class_students / half_divisor

    # L2
    additional_students = 10 # 10 more than half
    johnson_class_students = half_finley_class + additional_students

    # FA
    answer = johnson_class_students
    return answer