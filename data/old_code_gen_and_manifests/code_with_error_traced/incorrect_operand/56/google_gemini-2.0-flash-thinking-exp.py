def solve(
    time_part1: int = 25, # finished the first part of his assignment in 25 minutes
    multiplier_part2: int = 2, # took him twice as long to finish the second part
    total_time_hours: int = 2 # finish his assignment in 2 hours
):
    """Index: 56.
    Returns: the number of minutes Leo took to finish the third part of the assignment.
    """

    #: L1
    time_part2 = time_part1 * multiplier_part2 # eval: 50 = 25 * 2

    #: L2
    time_parts1_and_2 = total_time_hours + time_part2 # eval: 52 = 2 + 50

    #: L3
    total_time_minutes = total_time_hours * 60 # eval: 120 = 2 * 60

    #: L4
    time_part3 = total_time_minutes - time_parts1_and_2 # eval: 68 = 120 - 52

    #: FA
    answer = time_part3
    return answer # eval: return 68
