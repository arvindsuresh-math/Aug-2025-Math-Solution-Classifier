def solve():
    """Index: 6623.
    Returns: the time in minutes to load the compost.
    """
    # L1
    tractor_rate = 75 # 75 pounds per minute
    darrel_rate = 10 # 10 pounds per minute
    combined_rate = tractor_rate + darrel_rate

    # L2
    total_compost_needed = 2550 # 2550 pounds of compost
    time_to_load = total_compost_needed / combined_rate

    # FA
    answer = time_to_load
    return answer