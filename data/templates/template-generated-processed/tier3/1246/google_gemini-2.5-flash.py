def solve():
    """Index: 1246.
    Returns: the total time in hours the spaceship was not moving.
    """
    # L1
    first_travel_segment_1 = 10 # traveled for 10 hours
    first_travel_segment_2 = 10 # traveled for another 10 hours
    first_day_travel_hours = first_travel_segment_1 + first_travel_segment_2

    # L2
    first_stop_segment_1 = 3 # stopped for 3 hours
    first_stop_segment_2 = 1 # stopped for 1 hour
    first_day_stop_hours = first_stop_segment_1 + first_stop_segment_2

    # L3
    hours_per_day = 24 # 24 hours or 1 day
    total_hours_first_day = first_day_travel_hours + first_day_stop_hours

    # L4
    total_journey_days = 3 # entire journey took 3 days
    first_day_count = 1 # 1 first day
    remaining_journey_days = total_journey_days - first_day_count

    # L5
    remaining_journey_hours = remaining_journey_days * hours_per_day

    # L6
    travel_block_hours = 11 # every 11 hours of traveling
    break_block_hours = 1 # an hour’s break
    routine_block_hours = travel_block_hours + break_block_hours

    # L7
    remaining_days_stop_hours = remaining_journey_hours / routine_block_hours

    # L8
    total_not_moving_hours = remaining_days_stop_hours + first_day_stop_hours

    # FA
    answer = total_not_moving_hours
    return answer