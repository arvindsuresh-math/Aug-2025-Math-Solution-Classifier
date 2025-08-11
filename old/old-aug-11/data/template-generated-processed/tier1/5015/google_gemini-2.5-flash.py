def solve():
    """Index: 5015.
    Returns: the total number of miles cycled today by Jack and Peter.
    """
    # L1
    distance_store_to_peter = 50 # 50 miles to his friend Peter
    time_multiplier_home_to_store = 2 # twice as long to go from his home to the store
    distance_home_to_store = time_multiplier_home_to_store * distance_store_to_peter

    # L3
    distance_back_to_store = distance_store_to_peter + distance_store_to_peter

    # L4
    total_miles_cycled = distance_home_to_store + distance_store_to_peter + distance_back_to_store

    # FA
    answer = total_miles_cycled
    return answer