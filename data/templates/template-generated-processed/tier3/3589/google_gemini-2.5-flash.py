def solve():
    """Index: 3589.
    Returns: the number of hours faster the bigger sail is than the smaller one.
    """
    # L1
    total_distance = 200 # He plans to travel 200 miles
    speed_bigger_sail = 50 # When he uses his 24 square foot sail he goes 50 MPH
    time_bigger_sail = total_distance / speed_bigger_sail

    # L2
    speed_smaller_sail = 20 # When he uses his 12 square foot sail he goes 20 MPH
    time_smaller_sail = total_distance / speed_smaller_sail

    # L3
    time_difference = time_smaller_sail - time_bigger_sail

    # FA
    answer = time_difference
    return answer