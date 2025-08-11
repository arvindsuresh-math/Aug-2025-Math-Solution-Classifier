def solve():
    """Index: 3494.
    Returns: the total number of minutes Jack spends mopping.
    """
    # L1
    bathroom_area = 24 # bathroom floor is 24 square feet
    kitchen_area = 80 # kitchen floor is 80 square feet
    total_area_to_mop = bathroom_area + kitchen_area

    # L2
    mopping_rate = 8 # Jack can mop 8 square feet per minute
    time_spent_mopping = total_area_to_mop / mopping_rate

    # FA
    answer = time_spent_mopping
    return answer