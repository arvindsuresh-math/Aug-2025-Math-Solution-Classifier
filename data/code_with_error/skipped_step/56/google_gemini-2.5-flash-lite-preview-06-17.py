def solve(
    time_part_1: int = 25, # Leo finished the first part of his assignment in 25 minutes.
    time_multiplier_part_2: int = 2, # It took him twice as long to finish the second part.
    total_time_hours: int = 2 # If he was able to finish his assignment in 2 hours
):
    """Index: 56.
    Returns: the number of minutes Leo took to finish the third part of the assignment.
    """

    #: L1
    time_part_2 = time_part_1 * time_multiplier_part_2

    #: L2
    time_part_1_and_2 = time_part_1 + time_part_2

    #: L3

    #: L4
    time_part_3 = time_part_1 - time_part_1_and_2

    #: FA
    answer = time_part_3
    return answer