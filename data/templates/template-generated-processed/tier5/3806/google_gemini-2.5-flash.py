def solve():
    """Index: 3806.
    Returns: the cost of the eel.
    """
    # L1
    combined_cost = 200 # combined cost of one order each kind of sushi is $200
    eel_multiplier = 9 # eel for nine times that amount

    # L3
    jellyfish_coefficient_combined = 1 + eel_multiplier

    # L4
    jellyfish_cost = combined_cost / jellyfish_coefficient_combined

    # L5
    eel_cost = eel_multiplier * jellyfish_cost

    # FA
    answer = eel_cost
    return answer