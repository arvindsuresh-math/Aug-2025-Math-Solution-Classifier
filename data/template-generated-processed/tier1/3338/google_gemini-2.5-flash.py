def solve():
    """Index: 3338.
    Returns: the total time Nicky waited at the DMV.
    """
    # L1
    time_waiting_to_take_number = 20 # 20 minutes waiting to take a number
    quadruple_multiplier = 4 # quadruple that amount of time
    extra_wait_for_number = 14 # plus 14 minutes waiting for his number to be called
    time_waiting_for_number_called = quadruple_multiplier * time_waiting_to_take_number + extra_wait_for_number

    # L2
    total_wait_time = time_waiting_for_number_called + time_waiting_to_take_number

    # FA
    answer = total_wait_time
    return answer