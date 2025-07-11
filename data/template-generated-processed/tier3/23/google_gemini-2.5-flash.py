def solve():
    """Index: 23.
    Returns: the cost of each top.
    """
    # L1
    num_shorts = 5 # 5 pairs of shorts
    cost_per_short = 7 # for $7 each
    total_cost_shorts = num_shorts * cost_per_short

    # L2
    num_shoes = 2 # 2 pairs of shoes
    cost_per_shoe = 10 # for $10 each
    total_cost_shoes = num_shoes * cost_per_shoe

    # L3
    total_cost_shorts_shoes = total_cost_shorts + total_cost_shoes

    # L4
    total_spent = 75 # For $75 she bought
    cost_of_tops = total_spent - total_cost_shorts_shoes

    # L5
    num_tops = 4 # 4 tops
    cost_per_top = cost_of_tops / num_tops

    # FA
    answer = cost_per_top
    return answer