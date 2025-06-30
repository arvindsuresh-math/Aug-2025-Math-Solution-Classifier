def solve(
    budget: int = 200,  # Alexis went to a department store with a budget of $200
    shirt_cost: int = 30,  # spent $30 on a button-up shirt
    pants_cost: int = 46,  # $46 on suit pants
    coat_cost: int = 38,  # $38 on a suit coat
    socks_cost: int = 11,  # $11 on socks
    belt_cost: int = 18,  # $18 on a belt
    money_left: int = 16  # She has $16 left from her budget
):
    """Index: 8.
    Returns: the amount Alexis paid for the shoes."""

    #: L2
    other_items_total = shirt_cost + pants_cost + coat_cost + socks_cost + belt_cost # eval: 143 = 30 + 46 + 38 + 11 + 18

    #: L3
    total_spent = budget - money_left # eval: 184 = 200 - 16

    #: L4
    shoes_cost = total_spent - other_items_total # eval: 41 = 184 - 143

    #: FA
    answer = shoes_cost # eval: 41 = 41
    return answer # eval: return 41
