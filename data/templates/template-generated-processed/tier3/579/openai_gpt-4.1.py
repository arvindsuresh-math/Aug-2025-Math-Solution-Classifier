def solve():
    """Index: 579.
    Returns: the average number of leaves that fell per hour.
    """
    # L4
    first_hour_leaves = 7 # 7 leaves fall in the first hour
    second_hour_leaves = 4 # 4 leaves fall in the second hour
    third_hour_leaves = 4 # 4 leaves fall in the third hour
    total_leaves = first_hour_leaves + second_hour_leaves + third_hour_leaves

    # L5
    total_hours = 3 # 3 hours
    average_leaves_per_hour = total_leaves / total_hours

    # FA
    answer = average_leaves_per_hour
    return answer