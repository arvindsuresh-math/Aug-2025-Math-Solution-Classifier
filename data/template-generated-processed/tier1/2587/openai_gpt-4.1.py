def solve():
    """Index: 2587.
    Returns: the total miles Rocky ran in the first three days of training.
    """
    # L1
    day1_miles = 4 # run 4 miles on day one of training

    # L2
    day2_multiplier = 2 # double the miles for day 2
    day2_miles = day2_multiplier * day1_miles

    # L3
    day3_multiplier = 3 # triple the miles from day 2 for day 3
    day3_miles = day2_miles * day3_multiplier

    # L4
    total_miles = day1_miles + day2_miles + day3_miles

    # FA
    answer = total_miles
    return answer