def solve():
    """Index: 2736.
    Returns: the total vertical distance traveled by Paul in a week.
    """
    # L1
    trips_per_day = 3 # 3 trips out from and back to his apartment
    movements_per_trip = 2 # each trip involves going both down and up
    vertical_movements_per_day = trips_per_day * movements_per_trip

    # L2
    days_in_week = 7 # WK
    vertical_movements_per_week = vertical_movements_per_day * days_in_week

    # L3
    num_stories = 5 # 5th story apartment
    story_height_feet = 10 # each story is 10 feet tall
    feet_per_vertical_movement = num_stories * story_height_feet

    # L4
    total_vertical_distance = feet_per_vertical_movement * vertical_movements_per_week

    # FA
    answer = total_vertical_distance
    return answer