def solve():
    """Index: 1212.
    Returns: the total number of crackers Darren and Calvin bought altogether.
    """
    # L1
    darren_boxes = 4 # Darren bought 4 boxes of crackers
    crackers_per_box = 24 # Each box contained 24 crackers
    darren_crackers = crackers_per_box * darren_boxes

    # L2
    twice_darren_boxes = 2 * darren_boxes

    # L3
    calvin_boxes = twice_darren_boxes - 1 # Calvin bought one box less than twice as many boxes as Darren

    # L4
    calvin_crackers = calvin_boxes * crackers_per_box

    # L5
    total_crackers = calvin_crackers + darren_crackers

    # FA
    answer = total_crackers
    return answer