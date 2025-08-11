def solve():
    """Index: 5939.
    Returns: the total number of cans of food that was their goal per week.
    """
    # L1
    initial_cans_day1 = 20 # On the first day, 20 cans were collected
    daily_increase = 5 # increased by 5 each day
    cans_day2 = initial_cans_day1 + daily_increase

    # L2
    cans_day3 = cans_day2 + daily_increase

    # L3
    cans_day4 = cans_day3 + daily_increase

    # L4
    cans_day5 = cans_day4 + daily_increase

    # L5
    total_cans_per_week = initial_cans_day1 + cans_day2 + cans_day3 + cans_day4 + cans_day5

    # FA
    answer = total_cans_per_week
    return answer