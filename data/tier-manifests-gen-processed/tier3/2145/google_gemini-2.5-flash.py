def solve():
    """Index: 2145.
    Returns: the number of stop signs Rudolph encountered per mile.
    """
    # L1
    base_miles = 5 # 5 miles
    additional_miles = 2 # 2 more than 5 miles
    total_miles = base_miles + additional_miles

    # L2
    base_stop_signs = 17 # 17 stop signs
    less_stop_signs = 3 # 3 less than 17 stop signs
    total_stop_signs = base_stop_signs - less_stop_signs

    # L3
    stop_signs_per_mile = total_stop_signs / total_miles

    # FA
    answer = stop_signs_per_mile
    return answer