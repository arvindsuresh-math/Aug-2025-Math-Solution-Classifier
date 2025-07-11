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
    cost_of_shorts = num_shorts * price_per_short

    #: L2
    cost_of_shoes = num_shoes * price_per_shoe

    #: L3
    cost_shorts_and_shoes = cost_of_shorts * cost_of_shoes

    #: L4
    cost_of_tops = total_spent - cost_shorts_and_shoes

    #: L5
    price_per_top = cost_of_tops / num_tops

    #: FA
    answer = price_per_top
    return answer