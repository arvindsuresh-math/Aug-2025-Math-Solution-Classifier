def solve():
    """Index: 7142.
    Returns: the money Frank would have remaining.
    """
    # L1
    cheapest_lamp_cost = 20 # The cost of the cheapest lamp is $20
    times_more_expensive = 3 # the most expensive in the store is 3 times more expensive
    most_expensive_lamp_cost = cheapest_lamp_cost * times_more_expensive

    # L2
    frank_has_money = 90 # he currently has $90
    money_remaining = frank_has_money - most_expensive_lamp_cost

    # FA
    answer = money_remaining
    return answer