def solve():
    """Index: 184.
    Returns: the total number of positive Coronavirus cases after the third day.
    """
    # L1
    initial_cases = 2000 # 2000 positive cases on a particular day
    new_cases_day2 = 500 # increased by 500 on the second day
    after_day2_cases = initial_cases + new_cases_day2

    # L2
    recoveries_day2 = 50 # 50 recoveries
    after_day2_recoveries = after_day2_cases - recoveries_day2

    # L3
    new_cases_day3 = 1500 # total number of new cases spiked to 1500
    after_day3_cases = after_day2_recoveries + new_cases_day3

    # L4
    recoveries_day3 = 200 # 200 recoveries
    after_day3_recoveries = after_day3_cases - recoveries_day3

    # FA
    answer = after_day3_recoveries
    return answer