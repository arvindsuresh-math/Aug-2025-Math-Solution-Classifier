def solve():
    """Index: 2036.
    Returns: the number of pills Mr. Johnson is supposed to take a day.
    """
    # L1
    total_days = 30 # enough pills for 30 days
    fraction_taken_numerator = 4 # four-fifths of the days
    fraction_taken_denominator = 5 # four-fifths of the days
    days_taken = total_days * fraction_taken_numerator / fraction_taken_denominator

    # L2
    days_left = total_days - days_taken

    # L3
    pills_left = 12 # he has 12 pills left
    pills_per_day = pills_left / days_left

    # FA
    answer = pills_per_day
    return answer