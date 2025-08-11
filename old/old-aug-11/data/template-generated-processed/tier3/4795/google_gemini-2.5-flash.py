def solve():
    """Index: 4795.
    Returns: the total time James works in hours.
    """
    # L1
    num_bedrooms = 3 # 3 bedrooms
    time_per_bedroom_minutes = 20 # 20 minutes to clean
    time_to_clean_living_room_minutes = num_bedrooms * time_per_bedroom_minutes

    # L2
    minutes_per_hour = 60 # WK
    time_to_clean_living_room_hours = time_to_clean_living_room_minutes / minutes_per_hour

    # L3
    bathroom_time_multiplier = 2 # twice as long as the living room
    time_to_clean_bathroom_hours = time_to_clean_living_room_hours * bathroom_time_multiplier

    # L4
    time_to_clean_bedrooms_minutes = num_bedrooms * time_per_bedroom_minutes
    time_to_clean_bedrooms_hours = time_to_clean_bedrooms_minutes / minutes_per_hour
    total_inside_time_hours = time_to_clean_bedrooms_hours + time_to_clean_living_room_hours + time_to_clean_bathroom_hours

    # L5
    outside_time_multiplier = 2 # twice as long as cleaning the house
    time_to_clean_outside_hours = total_inside_time_hours * outside_time_multiplier

    # L6
    total_chores_time_hours = total_inside_time_hours + time_to_clean_outside_hours

    # L7
    james_share = 1 # He splits the chores
    num_siblings = 2 # 2 siblings
    total_people_splitting_chores = james_share + num_siblings

    # L8
    james_work_time_hours = total_chores_time_hours / total_people_splitting_chores

    # FA
    answer = james_work_time_hours
    return answer