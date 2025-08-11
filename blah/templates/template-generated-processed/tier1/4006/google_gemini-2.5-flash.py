def solve():
    """Index: 4006.
    Returns: the total cost Fabian spent on his new accessories.
    """
    # L1
    keyboard_multiplier = 3 # three times greater
    mouse_cost = 16 # mouse cost $16
    keyboard_cost = keyboard_multiplier * mouse_cost

    # L2
    total_cost = keyboard_cost + mouse_cost

    # FA
    answer = total_cost
    return answer