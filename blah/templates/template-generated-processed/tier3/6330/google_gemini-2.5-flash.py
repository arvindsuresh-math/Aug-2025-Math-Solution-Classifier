def solve():
    """Index: 6330.
    Returns: the distance Ezekiel had to hike on the third day.
    """
    # L1
    total_hike_distance = 50 # 50 kilometers of wilderness
    first_day_distance = 10 # covered 10 kilometers of steep mountainside
    remaining_after_day1 = total_hike_distance - first_day_distance

    # L2
    half_divisor = 2 # half the full hike distance
    second_day_distance = total_hike_distance / half_divisor

    # L3
    third_day_distance = remaining_after_day1 - second_day_distance

    # FA
    answer = third_day_distance
    return answer