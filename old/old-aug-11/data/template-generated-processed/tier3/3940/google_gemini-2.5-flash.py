def solve():
    """Index: 3940.
    Returns: the total time Helen spends hand washing her pillowcases in a year.
    """
    # L1
    weeks_per_wash_cycle = 4 # Every 4 weeks
    weeks_per_year = 52 # 52 weeks in a year
    wash_frequency_per_year = weeks_per_year / weeks_per_wash_cycle

    # L2
    time_per_wash = 30 # It takes 30 minutes to hand wash all of them
    total_time_per_year_minutes = time_per_wash * wash_frequency_per_year

    # FA
    answer = total_time_per_year_minutes
    return answer