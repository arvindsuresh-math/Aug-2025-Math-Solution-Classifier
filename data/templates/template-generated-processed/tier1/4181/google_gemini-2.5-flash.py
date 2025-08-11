def solve():
    """Index: 4181.
    Returns: the amount Hannah needs to save in the fifth week to reach her goal.
    """
    # L1
    initial_savings_week1 = 4 # saved $4
    multiplier_twice = 2 # twice as much
    savings_week2 = initial_savings_week1 * multiplier_twice

    # L2
    savings_week3 = savings_week2 * multiplier_twice

    # L3
    savings_week4 = savings_week3 * multiplier_twice

    # L4
    total_savings_four_weeks = initial_savings_week1 + savings_week2 + savings_week3 + savings_week4

    # L5
    goal_savings = 80 # save $80
    savings_fifth_week = goal_savings - total_savings_four_weeks

    # FA
    answer = savings_fifth_week
    return answer