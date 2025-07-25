def solve():
    """Index: 4886.
    Returns: the total hours Tom danced.
    """
    # L1
    times_per_week = 4 # 4 times a week
    hours_per_time = 2 # 2 hours at a time
    hours_per_week = times_per_week * hours_per_time

    # L2
    weeks_per_year = 52 # WK
    num_years = 10 # 10 years
    total_weeks = weeks_per_year * num_years

    # L3
    total_dance_hours = hours_per_week * total_weeks

    # FA
    answer = total_dance_hours
    return answer