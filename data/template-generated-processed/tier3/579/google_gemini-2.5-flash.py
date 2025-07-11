def solve():
    """Index: 579.
    Returns: the average number of leaves which fell per hour.
    """
    # L1
    leaves_first_hour = 7 # 7 leaves fall in the first hour

    # L2
    leaves_second_hour = 4 # For the second and third hour, the leaves fall at a rate of 4 per hour

    # L3
    leaves_third_hour = 4 # For the second and third hour, the leaves fall at a rate of 4 per hour

    # L4
    total_leaves = leaves_first_hour + leaves_second_hour + leaves_third_hour

    # L5
    total_hours = 3 # implied by "first hour", "second hour", "third hour"
    average_leaves_per_hour = total_leaves / total_hours

    # FA
    answer = average_leaves_per_hour
    return answer