def solve():
    """Index: 184.
    Returns: the total number of positive Coronavirus cases after the third day.
    """
    # L1
    initial_cases = 2000 # 2000 positive cases on a particular day
    new_cases_day2 = 500 # increased by 500 on the second day
    cases_after_day2_increase = initial_cases + new_cases_day2

    # L2
    recoveries_day2 = 50 # 50 recoveries
    cases_after_day2_recoveries = cases_after_day2_increase - recoveries_day2

    # L3
    new_cases_day3 = 1500 # new cases spiked to 1500
    cases_after_day3_increase = cases_after_day2_recoveries + new_cases_day3

    # L4
    recoveries_day3 = 200 # 200 recoveries
    total_cases_after_day3 = cases_after_day3_increase - recoveries_day3

    # FA
    answer = total_cases_after_day3
    return answer