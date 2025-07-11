def solve():
    """Index: 1160.
    Returns: how much longer it would take Julia to run 5 miles in her new shoes than her old ones.
    """
    # L1
    miles = 5 # run 5 miles
    old_shoe_mile_time = 10 # run a mile in 10 minutes
    old_shoe_total_time = miles * old_shoe_mile_time

    # L2
    new_shoe_mile_time = 13 # slowed her mile down to 13 minutes
    new_shoe_total_time = new_shoe_mile_time * miles

    # L3
    time_difference = new_shoe_total_time - old_shoe_total_time

    # FA
    answer = time_difference
    return answer