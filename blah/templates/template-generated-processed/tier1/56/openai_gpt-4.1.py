def solve():
    """Index: 56.
    Returns: the number of minutes Leo took to finish the third part of the assignment.
    """
    # L1
    first_part_minutes = 25 # finished the first part in 25 minutes
    second_part_multiplier = 2 # took him twice as long to finish the second part
    second_part_minutes = first_part_minutes * second_part_multiplier

    # L2
    first_two_parts_minutes = first_part_minutes + second_part_minutes

    # L3
    hours_total = 2 # finish his assignment in 2 hours
    minutes_per_hour = 60 # WK
    total_minutes = minutes_per_hour * hours_total

    # L4
    third_part_minutes = total_minutes - first_two_parts_minutes

    # FA
    answer = third_part_minutes
    return answer