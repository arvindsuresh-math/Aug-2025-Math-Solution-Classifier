def solve():
    """Index: 6816.
    Returns: the total time Harry's morning routine takes.
    """
    # L1
    time_for_coffee_bagel = 15 # 15 minutes to buy coffee and a bagel
    multiplier_for_reading_eating = 2 # twice that long
    time_for_reading_eating = time_for_coffee_bagel * multiplier_for_reading_eating

    # L2
    total_routine_time = time_for_reading_eating + time_for_coffee_bagel

    # FA
    answer = total_routine_time
    return answer