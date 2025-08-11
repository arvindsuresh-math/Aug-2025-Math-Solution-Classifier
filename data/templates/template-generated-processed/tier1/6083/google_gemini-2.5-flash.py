def solve():
    """Index: 6083.
    Returns: the value of the next roll needed to achieve the target average.
    """
    # L1
    num_previous_rolls = 10 # from the list of 10 rolls in the question
    total_rolls = num_previous_rolls + 1

    # L2
    target_average = 3 # average of all his rolls is a 3
    target_sum = target_average * total_rolls

    # L3
    # The solution's sum lists specific rolls that differ slightly from the question's list, but result in the same total.
    roll_sol_1 = 1 # rolls as listed in solution for sum calculation
    roll_sol_2 = 3 # rolls as listed in solution for sum calculation
    roll_sol_3 = 2 # rolls as listed in solution for sum calculation
    roll_sol_4 = 4 # rolls as listed in solution for sum calculation
    roll_sol_5 = 3 # rolls as listed in solution for sum calculation
    roll_sol_6 = 5 # rolls as listed in solution for sum calculation
    roll_sol_7 = 6 # rolls as listed in solution for sum calculation
    roll_sol_8 = 1 # rolls as listed in solution for sum calculation
    roll_sol_9 = 4 # rolls as listed in solution for sum calculation
    roll_sol_10 = 2 # rolls as listed in solution for sum calculation
    current_sum = roll_sol_1 + roll_sol_2 + roll_sol_3 + roll_sol_4 + roll_sol_5 + roll_sol_6 + roll_sol_7 + roll_sol_8 + roll_sol_9 + roll_sol_10

    # L4
    needed_roll = target_sum - current_sum

    # FA
    answer = needed_roll
    return answer