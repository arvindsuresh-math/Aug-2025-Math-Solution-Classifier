def solve(
    first_part_time: int = 25,  # Leo finished the first part of his assignment in 25 minutes
    total_assignment_time: int = 120,  # He was able to finish his assignment in 2 hours (120 minutes)
    second_part_multiplier: int = 2  # It took him twice as long to finish the second part
):
    """Index: 56.
    Returns: the number of minutes Leo took to finish the third part of the assignment.
    """
    #: L1
    second_part_time = first_part_time * second_part_multiplier

    #: L2
    first_and_second_part_time = first_part_time + second_part_time

    #: L3
    # total_assignment_time is already converted to minutes (2 hours = 120 minutes)

    #: L4
    third_part_time = total_assignment_time - first_and_second_part_time

    answer = third_part_time  # FINAL ANSWER
    return answer