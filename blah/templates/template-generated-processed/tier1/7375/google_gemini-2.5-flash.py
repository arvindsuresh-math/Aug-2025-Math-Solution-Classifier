def solve():
    """Index: 7375.
    Returns: the total time Carlos's laundry takes.
    """
    # L1
    num_loads = 2 # two loads
    time_per_load = 45 # 45 minutes per load
    washing_time = num_loads * time_per_load

    # L2
    drying_time = 75 # takes 75 minutes
    total_laundry_time = washing_time + drying_time

    # FA
    answer = total_laundry_time
    return answer