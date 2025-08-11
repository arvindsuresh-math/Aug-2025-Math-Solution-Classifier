def solve():
    """Index: 3686.
    Returns: the initial amount of money Blake gave to Connie.
    """
    # L1
    money_given_to_blake = 30000 # If Connie gave Blake $30,000
    share_divisor = 2 # half of all the money she got from the sale
    full_sale_value = money_given_to_blake * share_divisor

    # L2
    value_multiplier = 3 # land tripled in value
    initial_cost = full_sale_value / value_multiplier

    # FA
    answer = initial_cost
    return answer