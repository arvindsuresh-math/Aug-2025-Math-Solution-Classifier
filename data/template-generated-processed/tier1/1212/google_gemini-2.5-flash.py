def solve():
    """Index: 1212.
    Returns: the total number of crackers Darren and Calvin bought altogether.
    """
    # L1
    darren_boxes = 4 # Darren bought 4 boxes of crackers
    crackers_per_box = 24 # Each box contained 24 crackers
    darren_total_crackers = crackers_per_box * darren_boxes

    # L2
    multiplier_twice = 2 # twice as many boxes
    twice_darren_boxes = multiplier_twice * darren_boxes

    # L3
    calvin_less_than_twice = 1 # one box less than twice as many boxes
    calvin_boxes = twice_darren_boxes - calvin_less_than_twice

    # L4
    calvin_total_crackers = calvin_boxes * crackers_per_box

    # L5
    total_crackers_altogether = calvin_total_crackers + darren_total_crackers

    # FA
    answer = total_crackers_altogether
    return answer