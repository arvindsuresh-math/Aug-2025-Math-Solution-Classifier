def solve():
    """Index: 4193.
    Returns: the total minutes Hayden spends ironing over 4 weeks.
    """
    # L1
    shirt_ironing_time = 5 # 5 minutes ironing his button-up shirt
    pants_ironing_time = 3 # 3 minutes ironing his pants
    daily_ironing_time = shirt_ironing_time + pants_ironing_time

    # L2
    days_per_week = 5 # 5 days a week
    weekly_ironing_time = days_per_week * daily_ironing_time

    # L3
    num_weeks = 4 # over 4 weeks
    total_ironing_time = num_weeks * weekly_ironing_time

    # FA
    answer = total_ironing_time
    return answer