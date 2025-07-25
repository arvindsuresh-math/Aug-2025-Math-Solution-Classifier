def solve():
    """Index: 547.
    Returns: the total time everything took to renovate.
    """
    # L1
    bedroom_renovation_time = 4 # each bedroom takes 4 hours to renovate
    kitchen_longer_percent = 0.5 # 50% longer
    kitchen_extra_time = bedroom_renovation_time * kitchen_longer_percent

    # L2
    kitchen_total_time = bedroom_renovation_time + kitchen_extra_time

    # L3
    num_bedrooms = 3 # 3 bedrooms
    bedrooms_total_time = num_bedrooms * bedroom_renovation_time

    # L4
    kitchen_bedrooms_combined_time = bedrooms_total_time + kitchen_total_time

    # L5
    living_room_time_factor = 2 # twice as much time
    living_room_total_time = kitchen_bedrooms_combined_time * living_room_time_factor

    # L6
    total_renovation_time = kitchen_bedrooms_combined_time + living_room_total_time

    # FA
    answer = total_renovation_time
    return answer