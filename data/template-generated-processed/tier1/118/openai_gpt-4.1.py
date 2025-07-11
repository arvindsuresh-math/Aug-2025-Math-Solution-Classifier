def solve():
    """Index: 118.
    Returns: the number of objects Jeanette can juggle after 5 weeks.
    """
    # L1
    additional_per_week = 2 # she can juggle 2 more objects than the week before
    num_weeks = 5 # practices for 5 weeks
    total_additional = additional_per_week * num_weeks

    # L2
    initial_objects = 3 # starts out juggling 3 objects
    total_objects = total_additional + initial_objects

    # FA
    answer = total_objects
    return answer