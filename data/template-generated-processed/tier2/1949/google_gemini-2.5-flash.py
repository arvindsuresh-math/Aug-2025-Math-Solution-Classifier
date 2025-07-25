def solve():
    """Index: 1949.
    Returns: how much more money Albert needs.
    """
    # L1
    paintbrush_cost = 1.50 # paintbrush that costs $1.50
    paints_cost = 4.35 # set of paints that costs $4.35
    easel_cost = 12.65 # wooden easel that costs $12.65
    total_items_cost = paintbrush_cost + paints_cost + easel_cost

    # L2
    money_albert_has = 6.50 # Albert already has $6.50
    money_needed = total_items_cost - money_albert_has

    # FA
    answer = money_needed
    return answer