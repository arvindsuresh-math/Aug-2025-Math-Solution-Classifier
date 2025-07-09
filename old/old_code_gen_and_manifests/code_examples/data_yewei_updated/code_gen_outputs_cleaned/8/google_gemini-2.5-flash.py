def solve(
        budget: int = 200, # with a budget of $200
        cost_button_up_shirt: int = 30, # spent $30 on a button-up shirt
        cost_suit_pants: int = 46, # $46 on suit pants
        cost_suit_coat: int = 38, # $38 on a suit coat
        cost_socks: int = 11, # $11 on socks
        cost_belt: int = 18, # $18 on a belt
        remaining_budget: int = 16 # She has $16 left from her budget
    ):
    """Index: 8.
    Returns: the amount Alexis paid for the shoes.
    """
    #: L1
    # Let S be the amount Alexis paid for the shoes. (Conceptual step)

    #: L2
    known_expenses = cost_button_up_shirt + cost_suit_pants + cost_suit_coat + cost_socks + cost_belt

    #: L3
    total_spent = budget - remaining_budget

    #: L4
    cost_shoes = total_spent - known_expenses

    answer = cost_shoes # FINAL ANSWER
    return answer