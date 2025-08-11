def solve():
    """Index: 1444.
    Returns: twice the total number of high school credits the three have.
    """
    # L1
    emily_credits = 20 # Emily has 20 credits
    aria_multiplier = 2 # Aria has twice as many high school credits as Emily
    aria_credits = aria_multiplier * emily_credits

    # L2
    spencer_divisor = 2 # Emily has twice the number of high school credits Spencer has
    spencer_credits = emily_credits / spencer_divisor

    # L3
    total_credits = aria_credits + emily_credits + spencer_credits

    # L4
    final_multiplier = 2 # twice the total number
    final_answer_value = final_multiplier * total_credits

    # FA
    answer = final_answer_value
    return answer