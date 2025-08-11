def solve():
    """Index: 5456.
    Returns: the number of more boys than girls in the class.
    """
    # L1
    boys_ratio_part = 3 # ratio of boys to girls is 3:2
    girls_ratio_part = 2 # ratio of boys to girls is 3:2
    total_ratio_parts = boys_ratio_part + girls_ratio_part

    # L2
    total_students = 100 # 100 students in class
    students_per_part = total_students / total_ratio_parts

    # L3
    num_boys = students_per_part * boys_ratio_part

    # L4
    num_girls = total_students - num_boys

    # L5
    more_boys_than_girls = num_boys - num_girls

    # FA
    answer = more_boys_than_girls
    return answer