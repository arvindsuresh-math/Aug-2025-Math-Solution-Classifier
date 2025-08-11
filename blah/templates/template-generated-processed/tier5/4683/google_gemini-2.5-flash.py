def solve():
    """Index: 4683.
    Returns: the number of students in the Period 2 gym class.
    """
    # L3
    period1_students = 11 # There are 11 students in the Period 1 gym class
    fewer_than = 5 # 5 fewer than twice as many
    multiplier_for_twice = 2 # twice as many students
    intermediate_sum = period1_students + fewer_than

    # L4
    period2_students = intermediate_sum / multiplier_for_twice

    # FA
    answer = period2_students
    return answer