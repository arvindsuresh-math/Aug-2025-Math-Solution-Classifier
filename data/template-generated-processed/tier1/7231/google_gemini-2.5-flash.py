def solve():
    """Index: 7231.
    Returns: the remaining amount of Tyler's money.
    """
    # L1
    num_scissors = 8 # 8 scissors
    price_per_scissor = 5 # $5 each
    cost_scissors = num_scissors * price_per_scissor

    # L2
    num_erasers = 10 # 10 erasers
    price_per_eraser = 4 # $4 each
    cost_erasers = num_erasers * price_per_eraser

    # L3
    total_cost = cost_scissors + cost_erasers

    # L4
    initial_money = 100 # Tyler has $100
    remaining_money = initial_money - total_cost

    # FA
    answer = remaining_money
    return answer