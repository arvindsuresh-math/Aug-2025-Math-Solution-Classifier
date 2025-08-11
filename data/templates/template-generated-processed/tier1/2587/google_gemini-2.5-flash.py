def solve():
    """Index: 2587.
    Returns: the total miles Rocky ran in the first three days of training.
    """
    # L1
    day1_miles = 4 # 4 miles on day one of training

    # L2
    double_factor = 2 # double the miles
    day2_miles = double_factor * day1_miles

    # L3
    triple_factor = 3 # triple the miles from day 2
    day3_miles = day2_miles * triple_factor

    # L4
    total_miles = day1_miles + day2_miles + day3_miles

    # FA
    answer = total_miles
    return answer