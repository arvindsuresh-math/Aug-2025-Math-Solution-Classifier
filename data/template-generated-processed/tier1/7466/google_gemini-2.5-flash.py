def solve():
    """Index: 7466.
    Returns: how much more Janet spends on piano lessons than clarinet lessons in a year.
    """
    # L1
    clarinet_hourly_rate = 40 # $40/hour for 3 hours per week of clarinet lessons
    clarinet_hours_per_week = 3 # 3 hours per week of clarinet lessons
    clarinet_weekly_cost = clarinet_hourly_rate * clarinet_hours_per_week

    # L2
    piano_hourly_rate = 28 # $28/hour for 5 hours a week of piano lessons
    piano_hours_per_week = 5 # 5 hours a week of piano lessons
    piano_weekly_cost = piano_hourly_rate * piano_hours_per_week

    # L3
    weekly_difference = piano_weekly_cost - clarinet_weekly_cost

    # L4
    weeks_per_year = 52 # WK
    annual_difference = weekly_difference * weeks_per_year

    # FA
    answer = annual_difference
    return answer