def solve(
        first_part_time: int = 25,  # Leo finished the first part of his assignment in 25 minutes
        hours_to_complete: int = 2,  # he was able to finish his assignment in 2 hours
        second_part_multiplier: int = 2  # It took him twice as long to finish the second part
    ):
    """Index: 56.
    Returns: the number of minutes Leo took to finish the third part of the assignment.
    """

    #: L1
    second_part_time = first_part_time * second_part_multiplier # eval: 50 = 25 * 2

    #: L2
    first_and_second_part_time = first_part_time + second_part_time # eval: 75 = 25 + 50

    #: L3
    total_assignment_time = hours_to_complete * 60 # eval: 120 = 2 * 60

    #: L4
    third_part_time = total_assignment_time - first_and_second_part_time # eval: 45 = 120 - 75

    #: FA
    answer = third_part_time # eval: 45 = 45
    return answer # eval: return 45
