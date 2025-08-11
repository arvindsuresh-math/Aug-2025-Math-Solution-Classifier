def solve():
    """Index: 5065.
    Returns: the number of problems no one but Angela finished.
    """
    # L1
    martha_finished = 2 # Martha has finished 2
    multiplier = 4 # four times
    martha_times_four = multiplier * martha_finished

    # L2
    jenna_subtraction = 2 # minus 2
    jenna_finished = martha_times_four - jenna_subtraction

    # L3
    mark_divisor = 2 # half the number Jenna did
    mark_finished = jenna_finished / mark_divisor

    # L4
    total_friends_finished = martha_finished + jenna_finished + mark_finished

    # L5
    total_problems = 20 # Out of 20 problems
    angela_only_finished = total_problems - total_friends_finished

    # FA
    answer = angela_only_finished
    return answer