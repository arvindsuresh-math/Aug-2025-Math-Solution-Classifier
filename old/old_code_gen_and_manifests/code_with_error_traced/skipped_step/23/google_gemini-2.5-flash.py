def solve(
        total_spent: int = 75, # For $75 she bought
        num_shorts: int = 5, # 5 pairs of shorts
        price_per_short: int = 7, # for $7 each
        num_shoes: int = 2, # and 2 pairs of shoes
        price_per_shoe: int = 10, # for $10 each
        num_tops: int = 4 # She also bought 4 tops
    ):
    """Index: 23.
    Returns: the cost of each top.
    """

    #: L1
    cost_shorts = num_shorts * price_per_short # eval: 35 = 5 * 7

    #: L2
    cost_shoes = num_shoes * price_per_shoe # eval: 20 = 2 * 10

    #: L3

    #: L4
    cost_tops_total = total_spent - price_per_shoe # eval: 65 = 75 - 10

    #: L5
    cost_per_top = cost_tops_total / num_tops # eval: 16.25 = 65 / 4

    #: FA
    answer = cost_per_top
    return answer # eval: return 16.25
