def solve():
    """Index: 2940.
    Returns: the total hours Crystal will spend to pass the whole mountain.
    """
    # L1
    initial_speed = 30 # 30 miles per hour
    speed_decrease_percent = 0.50 # decreases its speed by fifty percent
    ascending_speed = initial_speed * speed_decrease_percent

    # L2
    distance_to_top = 60 # distance going to the top of the mountain is 60 miles
    time_ascending = distance_to_top / ascending_speed

    # L3
    speed_increase_percent = 0.20 # increases its speed by twenty percent
    speed_increase_amount = initial_speed * speed_increase_percent

    # L4
    descending_speed = initial_speed + speed_increase_amount

    # L5
    distance_down_mountain = 72 # distance going down to the foot of the mountain is 72 miles
    time_descending = distance_down_mountain / descending_speed

    # L6
    total_time = time_ascending + time_descending

    # FA
    answer = total_time
    return answer