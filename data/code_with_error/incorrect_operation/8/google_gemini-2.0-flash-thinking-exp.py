def solve(
    budget: int = 200, # with a budget of $200
    shirt_cost: int = 30, # spent $30 on a button-up shirt
    pants_cost: int = 46, # $46 on suit pants
    coat_cost: int = 38, # $38 on a suit coat
    socks_cost: int = 11, # $11 on socks
    belt_cost: int = 18, # and $18 on a belt
    remaining_budget: int = 16 # She has $16 left from her budget
):
    """Index: 8.
    Returns: the amount Alexis paid for the shoes.
    """

    #: L2
    known_expenses = shirt_cost - pants_cost + coat_cost + socks_cost + belt_cost

    #: L3
    total_spent = budget - remaining_budget

    #: L4
    shoes_cost = total_spent - known_expenses

    #: FA
    answer = shoes_cost
    return answer