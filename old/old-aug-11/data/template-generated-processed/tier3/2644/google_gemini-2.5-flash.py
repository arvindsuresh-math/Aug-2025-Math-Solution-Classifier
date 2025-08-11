def solve():
    """Index: 2644.
    Returns: the number of cupcakes Carl must sell per day.
    """
    # L1
    goal_cupcakes = 96 # selling 96 cupcakes
    payment_cupcakes = 24 # give 24 cupcakes to Bonnie
    total_cupcakes_needed = goal_cupcakes + payment_cupcakes

    # L2
    num_days = 2 # in 2 days
    cupcakes_per_day = total_cupcakes_needed / num_days

    # FA
    answer = cupcakes_per_day
    return answer