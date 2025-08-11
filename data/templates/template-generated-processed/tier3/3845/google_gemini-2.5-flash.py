def solve():
    """Index: 3845.
    Returns: the total number of mushrooms picked over three days.
    """
    # L1
    total_sold_first_day = 58 # sold all the mushrooms they picked on the first day for a total of $58
    price_per_mushroom = 2 # price per mushroom was $2
    mushrooms_first_day = total_sold_first_day / price_per_mushroom

    # L2
    mushrooms_second_day = 12 # picked 12 mushrooms
    cumulative_mushrooms_after_second_day = mushrooms_first_day + mushrooms_second_day

    # L3
    double_factor = 2 # double the mushrooms
    mushrooms_third_day = double_factor * mushrooms_second_day

    # L4
    total_mushrooms_picked = cumulative_mushrooms_after_second_day + mushrooms_third_day

    # FA
    answer = total_mushrooms_picked
    return answer