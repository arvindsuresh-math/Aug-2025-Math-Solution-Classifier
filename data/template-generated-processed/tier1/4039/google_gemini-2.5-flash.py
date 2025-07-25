def solve():
    """Index: 4039.
    Returns: the total number of hours spent on the road trip.
    """
    # L1
    jenna_distance = 200 # driving the first 200 miles
    jenna_speed = 50 # Jenna drives 50 miles per hour
    jenna_driving_time = jenna_distance / jenna_speed

    # L2
    friend_distance = 100 # her friend will drive the last 100 miles
    friend_speed = 20 # her friend drives 20 miles per hour
    friend_driving_time = friend_distance / friend_speed

    # L3
    break_duration_per_break = 30 # 2 30-minute breaks
    total_break_minutes = break_duration_per_break + break_duration_per_break

    # L4
    minutes_per_hour = 60 # WK
    total_break_hours = total_break_minutes / minutes_per_hour

    # L5
    total_trip_hours = total_break_hours + jenna_driving_time + friend_driving_time

    # FA
    answer = total_trip_hours
    return answer