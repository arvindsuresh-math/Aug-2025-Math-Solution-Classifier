def solve():
    """Index: 933.
    Returns: the total number of feet John climbed.
    """
    # L1
    first_steps = 20 # The first staircase has 20 steps
    second_multiplier = 2 # The next has twice as many steps as the first
    second_steps = first_steps * second_multiplier

    # L2
    third_subtract = 10 # The final staircase has 10 fewer steps than the second one
    third_steps = second_steps - third_subtract

    # L3
    total_steps = first_steps + second_steps + third_steps

    # L4
    step_height = 0.5 # Each step is 0.5 feet
    total_feet = total_steps * step_height

    # FA
    answer = total_feet
    return answer