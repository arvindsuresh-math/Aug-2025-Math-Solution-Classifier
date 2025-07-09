def solve(
    budget: int = 200,  # Alexis has a budget of $200
    cost_shirt: int = 30,  # spent $30 on a button-up shirt
    cost_pants: int = 46,  # $46 on suit pants
    cost_coat: int = 38,  # $38 on a suit coat
    cost_socks: int = 11,  # $11 on socks
    cost_belt: int = 18,  # $18 on a belt
    money_left: int = 16  # She has $16 left from her budget
):
    """Index: 8.
    Returns: the amount Alexis paid for the shoes.
    """

    #: L2
    total_known_costs = cost_shirt + cost_pants + cost_coat + cost_socks + cost_belt

    #: L3
    total_spent = budget - money_left

    #: L4
    cost_shoes = total_spent - total_known_costs

    #: FA
    answer = cost_shoes
    return answer