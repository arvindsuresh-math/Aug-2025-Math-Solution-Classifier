def solve():
    """Index: 2992.
    Returns: the cost of each sandwich in dollars.
    """
    # L1
    cost_per_drink = 4 # drinks cost $4 each
    num_drinks = 2 # buys 2 drinks
    total_drink_cost = cost_per_drink * num_drinks

    # L2
    total_spending = 26 # spends a total of $26
    total_sandwich_cost = total_spending - total_drink_cost

    # L3
    num_sandwiches = 3 # buys a sandwich to eat now, one for the road, and one for in the evening
    cost_per_sandwich = total_sandwich_cost / num_sandwiches

    # FA
    answer = cost_per_sandwich
    return answer