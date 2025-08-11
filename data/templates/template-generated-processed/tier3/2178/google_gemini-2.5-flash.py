def solve():
    """Index: 2178.
    Returns: the final worth of Ben's lawnmower.
    """
    # L1
    initial_cost = 100 # He paid $100 for it
    first_drop_percentage_numerator = 25 # dropped by about 25%
    percentage_denominator = 100 # WK
    first_value_drop = (first_drop_percentage_numerator / percentage_denominator) * initial_cost

    # L2
    value_after_first_drop = initial_cost - first_value_drop

    # L3
    second_drop_percentage_numerator = 20 # dropped another 20%
    second_value_drop = (second_drop_percentage_numerator / percentage_denominator) * value_after_first_drop

    # L4
    final_worth = value_after_first_drop - second_value_drop

    # FA
    answer = final_worth
    return answer