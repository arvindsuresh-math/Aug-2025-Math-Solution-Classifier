def solve():
    """Index: 2272.
    Returns: the average number of employees hired per week.
    """
    # L1
    employees_fourth_week = 400 # the number of employees on the fourth week was 400
    twice_factor = 2 # twice the number
    employees_third_week = employees_fourth_week / twice_factor

    # L2
    fewer_than_second_week = 150 # 150 fewer employees on the second week
    employees_second_week = employees_third_week - fewer_than_second_week

    # L3
    more_than_second_week = 200 # 200 more employees on the first week
    employees_first_week = employees_second_week + more_than_second_week

    # L4
    total_employees = employees_first_week + employees_second_week + employees_third_week + employees_fourth_week

    # L5
    number_of_weeks = 4 # WK
    average_employees_per_week = total_employees / number_of_weeks

    # FA
    answer = average_employees_per_week
    return answer