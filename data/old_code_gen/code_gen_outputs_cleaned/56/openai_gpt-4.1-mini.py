def solve(
    time_first_part: int = 25,  # finished the first part of his assignment in 25 minutes
    time_multiplier_second_part: int = 2,  # took him twice as long to finish the second part
    total_time_hours: int = 2  # finished his assignment in 2 hours
):
    """Index: 56.
    Returns: the time in minutes Leo took to finish the third part of the assignment.
    """
    #: L1
    time_second_part = time_first_part * time_multiplier_second_part

    #: L2
    time_first_and_second = time_first_part + time_second_part

    #: L3
    total_time_minutes = total_time_hours * 60

    #: L4
    time_third_part = total_time_minutes - time_first_and_second

    answer = time_third_part  # FINAL ANSWER
    return answer