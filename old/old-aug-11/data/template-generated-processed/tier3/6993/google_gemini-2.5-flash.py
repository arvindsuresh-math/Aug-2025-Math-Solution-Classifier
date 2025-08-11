def solve():
    """Index: 6993.
    Returns: the number of hours John has to spare after painting.
    """
    # L1
    wall_length = 2 # 2 meters
    wall_height = 3 # 3 meters
    wall_area = wall_length * wall_height

    # L2
    paint_rate_minutes_per_sq_meter = 10 # 1 square meter every 10 minutes
    time_per_wall_minutes = wall_area * paint_rate_minutes_per_sq_meter

    # L3
    minutes_per_hour = 60 # WK
    time_per_wall_hours = time_per_wall_minutes / minutes_per_hour

    # L4
    num_walls = 5 # 5 walls
    total_paint_time_hours = num_walls * time_per_wall_hours

    # L5
    total_time_available_hours = 10 # 10 hours to paint everything
    hours_left = total_time_available_hours - total_paint_time_hours

    # FA
    answer = hours_left
    return answer