def solve():
    """Index: 2104.
    Returns: the total time Bill spends preparing for and cooking the five omelets.
    """
    # L1
    num_peppers = 4 # chop up four peppers
    minutes_per_pepper = 3 # 3 minutes to chop a pepper
    pepper_time = num_peppers * minutes_per_pepper

    # L2
    num_onions = 2 # two onions
    minutes_per_onion = 4 # 4 minutes to chop an onion
    onion_time = num_onions * minutes_per_onion

    # L3
    minutes_to_cook = 5 # 5 minutes to assemble and cook the omelet
    minutes_to_grate_cheese = 1 # 1 minute to grate enough cheese for one omelet
    time_per_omelet = minutes_to_cook + minutes_to_grate_cheese

    # L4
    num_omelets = 5 # five omelets
    total_omelet_time = num_omelets * time_per_omelet

    # L5
    total_time = total_omelet_time + pepper_time + onion_time

    # FA
    answer = total_time
    return answer