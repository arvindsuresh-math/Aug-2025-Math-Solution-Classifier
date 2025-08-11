def solve():
    """Index: 5935.
    Returns: the total time Kim spent away from home in hours.
    """
    # L1
    initial_distance = 30 # 30 miles to her friend's house
    detour_percentage = 0.2 # 20% longer
    detour_extra_miles = initial_distance * detour_percentage

    # L2
    return_trip_distance = initial_distance + detour_extra_miles

    # L3
    total_drive_distance = initial_distance + return_trip_distance

    # L4
    speed = 44 # speed of 44 mph
    total_drive_time_hours = total_drive_distance / speed

    # L5
    friend_house_minutes = 30 # 30 minutes at her friend's house
    minutes_per_hour = 60 # WK
    friend_house_time_hours = friend_house_minutes / minutes_per_hour

    # L6
    total_time_away = total_drive_time_hours + friend_house_time_hours

    # FA
    answer = total_time_away
    return answer