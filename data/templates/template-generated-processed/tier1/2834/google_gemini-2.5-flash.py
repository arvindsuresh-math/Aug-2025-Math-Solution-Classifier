def solve():
    """Index: 2834.
    Returns: the total number of math problems Marvin and Arvin have practiced altogether.
    """
    # L1
    marvin_solved_yesterday = 40 # Marvin solved 40 math problems yesterday
    marvin_today_multiplier = 3 # three times as many
    marvin_solved_today = marvin_solved_yesterday * marvin_today_multiplier

    # L2
    marvin_total_problems = marvin_solved_today + marvin_solved_yesterday

    # L3
    arvin_multiplier = 2 # twice as many math problems
    arvin_total_problems = marvin_total_problems * arvin_multiplier

    # L4
    total_problems_together = arvin_total_problems + marvin_total_problems

    # FA
    answer = total_problems_together
    return answer