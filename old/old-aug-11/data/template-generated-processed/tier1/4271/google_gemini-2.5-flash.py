def solve():
    """Index: 4271.
    Returns: the duration of the walk from the Park Office to the Lake Park restaurant.
    """
    # L1
    time_to_hidden_lake = 15 # 15 minutes for Dante to go to Hidden Lake
    time_back_to_office = 7 # 7 minutes to walk back to the Park Office
    time_round_trip = time_to_hidden_lake + time_back_to_office

    # L2
    total_time_gone = 32 # been gone from the Park Office 32 minutes altogether
    time_to_restaurant = total_time_gone - time_round_trip

    # FA
    answer = time_to_restaurant
    return answer