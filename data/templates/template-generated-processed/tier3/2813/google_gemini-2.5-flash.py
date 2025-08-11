def solve():
    """Index: 2813.
    Returns: the total amount Leila spent altogether.
    """
    # L1
    auto_cost = 350 # fixing her automobile cost $350
    more_than_thrice = 50 # $50 more than thrice the amount
    auto_cost_minus_extra = auto_cost - more_than_thrice

    # L2
    thrice_factor = 3 # thrice the amount
    supermarket_cost = auto_cost_minus_extra / thrice_factor

    # L3
    total_spent = supermarket_cost + auto_cost

    # FA
    answer = total_spent
    return answer