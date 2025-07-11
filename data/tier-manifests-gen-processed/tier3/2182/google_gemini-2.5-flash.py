def solve():
    """Index: 2182.
    Returns: the total number of customers served from 4 pm - 6 pm.
    """
    # L1
    minutes_per_hour = 60 # WK
    block_duration_minutes = 15 # every 15 minutes
    num_15_min_blocks_per_hour = minutes_per_hour / block_duration_minutes

    # L2
    peak_cars_per_block = 12 # 12 cars every 15 minutes
    peak_cars_per_hour = peak_cars_per_block * num_15_min_blocks_per_hour

    # L3
    off_peak_cars_per_block = 8 # 8 cars every 15 minutes
    off_peak_cars_per_hour = off_peak_cars_per_block * num_15_min_blocks_per_hour

    # L4
    total_cars_served = off_peak_cars_per_hour + peak_cars_per_hour

    # FA
    answer = total_cars_served
    return answer