def solve():
    """Index: 1569.
    Returns: the time in hours it takes to row the lake.
    """
    # L1
    side_length = 15 # Each side of the lake is 15 miles
    sides_of_square = 4 # WK
    perimeter = sides_of_square * side_length

    # L2
    minutes_per_hour = 60 # WK
    swim_time_minutes_per_mile = 20 # 20 minutes to swim 1 mile
    swim_speed_mph = minutes_per_hour / swim_time_minutes_per_mile

    # L3
    rowing_speed_multiplier = 2 # twice the speed he can swim
    row_speed_mph = swim_speed_mph * rowing_speed_multiplier

    # L4
    time_to_row_lake_hours = perimeter / row_speed_mph

    # FA
    answer = time_to_row_lake_hours
    return answer