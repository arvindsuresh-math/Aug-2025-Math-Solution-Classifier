def solve():
    """Index: 56.
    Returns: the number of minutes Leo finished the third part of the assignment.
    """
    # L1
    first_part_minutes = 25 # finished the first part of his assignment in 25 minutes
    multiplier_for_second_part = 2 # took him twice as long to finish the second part
    second_part_minutes = first_part_minutes * multiplier_for_second_part

    # L2
    first_and_second_parts_minutes = first_part_minutes + second_part_minutes

    # L3
    minutes_per_hour = 60 # WK
    total_hours = 2 # finish his assignment in 2 hours
    total_minutes_assignment = minutes_per_hour * total_hours

    # L4
    third_part_minutes = total_minutes_assignment - first_and_second_parts_minutes

    # FA
    answer = third_part_minutes
    return answer