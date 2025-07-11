def solve():
    """Index: 2898.
    Returns: the total time in hours for the elevator to reach the bottom.
    """
    # L1
    num_floors_next_segment = 5 # next 5 floors
    minutes_per_floor_next_segment = 5 # 5 minutes per floor
    time_next_segment = num_floors_next_segment * minutes_per_floor_next_segment

    # L2
    num_floors_final_segment = 5 # final 5 floors
    minutes_per_floor_final_segment = 16 # 16 minutes per floor
    time_final_segment = num_floors_final_segment * minutes_per_floor_final_segment

    # L3
    time_first_half = 15 # It takes 15 minutes for the elevator to travel down the first half of the floors
    total_minutes = time_first_half + time_next_segment + time_final_segment

    # L4
    minutes_per_hour = 60 # WK
    total_hours = total_minutes / minutes_per_hour

    # FA
    answer = total_hours
    return answer