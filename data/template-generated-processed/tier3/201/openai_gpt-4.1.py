def solve():
    """Index: 201.
    Returns: the average number of apples Archibald eats per week over 7 weeks.
    """
    # L1
    days_per_week = 7 # WK
    weeks1 = 2 # first two weeks
    apples_per_day1 = 1 # 1 apple a day for two weeks
    apples_first_two_weeks = days_per_week * weeks1 * apples_per_day1

    # L2
    apples_next_three_weeks = apples_first_two_weeks # eats the same number as the first two weeks

    # L3
    weeks3 = 2 # final two weeks
    apples_per_day3 = 3 # 3 apples a day
    apples_final_two_weeks = days_per_week * weeks3 * apples_per_day3

    # L4
    total_apples = apples_first_two_weeks + apples_next_three_weeks + apples_final_two_weeks

    # L5
    total_weeks = weeks1 + 3 + weeks3 # 2 + 3 + 2 = 7
    average_apples_per_week = total_apples / total_weeks

    # FA
    answer = average_apples_per_week
    return answer