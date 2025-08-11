def solve():
    """Index: 5851.
    Returns: the total number of crickets Gilbert will eat.
    """
    # L1
    total_weeks = 15 # over 15 weeks
    temp_90_percent_decimal = 0.8 # 80% of the time
    temp_90_percent_text = 80 # 80% of the time
    weeks_at_90_deg = temp_90_percent_decimal * total_weeks

    # L2
    weeks_at_100_deg = total_weeks - weeks_at_90_deg

    # L3
    crickets_per_week_90_deg = 4 # eats 4 crickets per week
    crickets_90_deg_total = weeks_at_90_deg * crickets_per_week_90_deg

    # L4
    twice_factor = 2 # twice as many crickets per week
    crickets_per_week_100_deg = twice_factor * crickets_per_week_90_deg

    # L5
    crickets_100_deg_total = crickets_per_week_100_deg * weeks_at_100_deg

    # L6
    total_crickets = crickets_90_deg_total + crickets_100_deg_total

    # FA
    answer = total_crickets
    return answer