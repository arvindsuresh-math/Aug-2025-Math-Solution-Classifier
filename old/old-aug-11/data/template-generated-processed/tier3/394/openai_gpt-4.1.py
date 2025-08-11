def solve():
    """Index: 394.
    Returns: the number of nights 5 boxes of crackers will last Chad.
    """
    # L1
    crackers_per_sandwich = 2 # 2 crackers with a scoop of peanut butter
    sandwiches_per_night = 5 # 5 of these crackers a night before bed
    crackers_per_night = crackers_per_sandwich * sandwiches_per_night

    # L2
    sleeves_per_box = 4 # 4 sleeves
    crackers_per_sleeve = 28 # each sleeve holding 28 crackers
    crackers_per_box = sleeves_per_box * crackers_per_sleeve

    # L3
    number_of_boxes = 5 # 5 boxes of crackers
    total_crackers = crackers_per_box * number_of_boxes

    # L4
    nights = total_crackers // crackers_per_night

    # FA
    answer = nights
    return answer