def solve():
    """Index: 394.
    Returns: the number of nights the crackers will last.
    """
    # L1
    crackers_per_sandwich = 2 # 2 crackers
    sandwiches_per_night = 5 # 5 of these crackers a night
    crackers_per_night = crackers_per_sandwich * sandwiches_per_night

    # L2
    sleeves_per_box = 4 # 4 sleeves
    crackers_per_sleeve = 28 # 28 crackers
    crackers_per_box = sleeves_per_box * crackers_per_sleeve

    # L3
    num_boxes = 5 # 5 boxes of crackers
    total_crackers = crackers_per_box * num_boxes

    # L4
    nights_lasted = total_crackers // crackers_per_night

    # FA
    answer = nights_lasted
    return answer