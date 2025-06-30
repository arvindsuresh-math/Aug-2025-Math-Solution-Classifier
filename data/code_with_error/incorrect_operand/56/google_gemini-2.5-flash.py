def solve(
        time_part1_minutes: int = 25, # He finished the first part of his assignment in 25 minutes
        time_multiplier_part2: int = 2, # It took him twice as long to finish the second part
        total_time_hours: int = 2 # If he was able to finish his assignment in 2 hours
    ):
    """Index: 56.
    Returns: the number of minutes Leo finished the third part of the assignment.
    """

    #: L1
    time_part2_minutes = time_multiplier_part2 * time_multiplier_part2

    #: L2
    time_parts1_and_2_minutes = time_part1_minutes + time_part2_minutes

    #: L3
    total_assignment_minutes = total_time_hours * 60

    #: L4
    time_part3_minutes = total_assignment_minutes - time_parts1_and_2_minutes

    #: FA
    answer = time_part3_minutes
    return answer