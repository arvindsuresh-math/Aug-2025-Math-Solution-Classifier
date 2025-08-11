def solve():
    """Index: 4783.
    Returns: the number of pills Ryan needs to take per week.
    """
    # L1
    daily_recommended_vitamin_a = 200 # The recommended daily serving of Vitamin A is 200 mg
    days_in_week = 7 # WK
    weekly_recommended_vitamin_a = days_in_week * daily_recommended_vitamin_a

    # L2
    mg_per_pill = 50 # Each pill has 50 mg of Vitamin A
    pills_needed_weekly = weekly_recommended_vitamin_a / mg_per_pill

    # FA
    answer = pills_needed_weekly
    return answer