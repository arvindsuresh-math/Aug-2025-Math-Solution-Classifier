def solve():
    """Index: 1080.
    Returns: the number of men in the engineering department.
    """
    # L1
    total_percentage = 100 # WK
    men_percentage = 70 # 70% of the students are men
    women_percentage = total_percentage - men_percentage

    # L2
    women_count = 180 # 180 are women
    percentage_per_unit = 1 # WK
    students_per_percent = women_count / women_percentage

    # L3
    men_count = students_per_percent * men_percentage

    # FA
    answer = men_count
    return answer