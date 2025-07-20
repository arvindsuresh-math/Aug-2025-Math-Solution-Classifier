def solve():
    """Index: 5140.
    Returns: 40% of the number of students who entered the bus.
    """
    # L1
    students_after_stop = 58 # there were 58 students on the bus
    students_before_stop = 28 # There were 28 students inside a bus
    students_entered = students_after_stop - students_before_stop

    # L2
    percentage_numerator = 40 # 40% of the number of students
    percentage_denominator = 100 # 40% of the number of students
    result = (percentage_numerator / percentage_denominator) * students_entered

    # FA
    answer = result
    return answer