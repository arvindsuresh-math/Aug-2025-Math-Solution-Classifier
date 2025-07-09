def solve(
    total_spent: int = 75, # For $75 she bought
    num_shorts: int = 5, # 5 pairs of shorts
    price_shorts: int = 7, # for $7 each
    num_shoes: int = 2, # and 2 pairs of shoes
    price_shoes: int = 10, # for $10 each
    num_tops: int = 4 # She also bought 4 tops
):
    """Index: 23.
    Returns: the cost of each top.
    """
    #: L1
    cost_shorts = num_shorts * price_shorts

    #: L2
    cost_shoes = num_shoes * price_shoes

    #: L3
    cost_shorts_and_shoes = cost_shorts + cost_shoes

    #: L4
    cost_tops = total_spent - cost_shorts_and_shoes

    #: L5
    price_each_top = cost_tops / num_tops

    answer = price_each_top # FINAL ANSWER
    return answer