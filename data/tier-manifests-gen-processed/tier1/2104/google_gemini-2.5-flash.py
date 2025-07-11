def solve():
    """Index: 2104.
    Returns: the total time Bill will spend preparing for and cooking the five omelets.
    """
    # L1
    num_peppers = 4 # chop up four peppers
    time_per_pepper = 3 # 3 minutes to chop a pepper
    total_pepper_chop_time = num_peppers * time_per_pepper

    # L2
    num_onions = 2 # two onions
    time_per_onion = 4 # 4 minutes to chop an onion
    total_onion_chop_time = num_onions * time_per_onion

    # L3
    time_to_cook_omelet = 5 # 5 minutes to assemble and cook the omelet
    time_to_grate_cheese_per_omelet = 1 # 1 minute to grate enough cheese for one omelet
    combined_time_per_omelet = time_to_cook_omelet + time_to_grate_cheese_per_omelet

    # L4
    num_omelets = 5 # five omelets
    total_omelet_cook_time = num_omelets * combined_time_per_omelet

    # L5
    total_time_spent = total_omelet_cook_time + total_pepper_chop_time + total_onion_chop_time

    # FA
    answer = total_time_spent
    return answer