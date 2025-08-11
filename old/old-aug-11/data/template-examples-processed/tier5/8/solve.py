def solve():
    """Index: 8.
    Returns: the amount Alexis paid for the shoes.
    """
    # L2
    shirt_cost = 30 # spent $30 on a button-up shirt
    pants_cost = 46 # $46 on suit pants
    coat_cost = 38 # $38 on a suit coat
    socks_cost = 11 # $11 on socks
    belt_cost = 18 # $18 on a belt
    other_items_total = shirt_cost + pants_cost + coat_cost + socks_cost + belt_cost

    # L3
    budget = 200 # budget of $200
    money_left = 16 # has $16 left from her budget
    total_spent = budget - money_left

    # L4
    shoes_cost = total_spent - other_items_total

    # FA
    answer = shoes_cost
    return answer