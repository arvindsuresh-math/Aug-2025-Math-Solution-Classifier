def solve():
    """Index: 5931.
    Returns: the time it takes Jake to bike to the water park in hours.
    """
    # L1
    dad_total_trip_minutes = 30 # 30 minutes
    half_divisor = 2 # half that journey
    dad_half_trip_minutes = dad_total_trip_minutes / half_divisor

    # L2
    minutes_per_hour = 60 # WK
    dad_half_trip_hours = dad_half_trip_minutes / minutes_per_hour

    # L3
    dad_speed_part1 = 28 # 28 miles per hour
    distance_part1 = dad_half_trip_hours * dad_speed_part1

    # L4
    dad_speed_part2 = 60 # 60 miles per hour
    distance_part2 = dad_half_trip_hours * dad_speed_part2

    # L5
    total_distance_to_park = distance_part1 + distance_part2

    # L6
    jake_bike_speed = 11 # Jake can bike 11 miles per hour
    jake_bike_time_hours = total_distance_to_park / jake_bike_speed

    # FA
    answer = jake_bike_time_hours
    return answer