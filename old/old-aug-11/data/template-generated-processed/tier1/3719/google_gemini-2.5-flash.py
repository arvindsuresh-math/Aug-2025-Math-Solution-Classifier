def solve():
    """Index: 3719.
    Returns: the number of problems Georgia has left to solve.
    """
    # L1
    total_problems = 75 # 75 problems on it
    initial_completed = 10 # completed 10 problems
    remaining_after_initial = total_problems - initial_completed

    # L2
    multiplier_twice = 2 # twice as many problems
    completed_second_batch = initial_completed * multiplier_twice

    # L3
    total_completed = initial_completed + completed_second_batch

    # L4
    problems_left = total_problems - total_completed

    # FA
    answer = problems_left
    return answer