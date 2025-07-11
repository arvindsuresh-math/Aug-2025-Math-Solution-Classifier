def solve():
    """Index: 118.
    Returns: the total number of objects Jeanette can juggle.
    """
    # L1
    additional_objects_per_week = 2 # 2 more objects
    weeks_practiced = 5 # practices for 5 weeks
    total_additional_objects = additional_objects_per_week * weeks_practiced

    # L2
    initial_objects = 3 # starts out juggling 3 objects
    final_objects = total_additional_objects + initial_objects

    # FA
    answer = final_objects
    return answer