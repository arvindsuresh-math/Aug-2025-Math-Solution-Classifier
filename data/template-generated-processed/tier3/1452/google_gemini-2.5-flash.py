def solve():
    """Index: 1452.
    Returns: how much earlier Abel reaches the destination in minutes.
    """
    # L1
    distance = 1000 # 1000 miles away
    abel_speed = 50 # driving 50 miles per hour
    abel_travel_hours = distance / abel_speed

    # L2
    alice_speed = 40 # traveling 40 miles per hour
    alice_travel_hours = distance / alice_speed

    # L3
    minutes_per_hour = 60 # 60 minutes in an hour
    abel_travel_minutes = abel_travel_hours * minutes_per_hour

    # L4
    alice_travel_minutes = alice_travel_hours * minutes_per_hour

    # L5
    time_difference_simultaneous = alice_travel_minutes - abel_travel_minutes

    # L6
    abel_head_start_hours = 1 # An hour later Alice leaves
    final_time_difference = time_difference_simultaneous + (abel_head_start_hours * minutes_per_hour)

    # FA
    answer = final_time_difference
    return answer