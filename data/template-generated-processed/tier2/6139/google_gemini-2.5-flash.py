def solve():
    """Index: 6139.
    Returns: how much more money Rose needs.
    """
    # L1
    paintbrush_cost = 2.40 # paintbrush that costs $2.40
    paints_cost = 9.20 # set of paints that costs $9.20
    easel_cost = 6.50 # easel that costs $6.50
    total_cost_items = paintbrush_cost + paints_cost + easel_cost

    # L2
    money_rose_has = 7.10 # Rose already has $7.10
    money_needed = total_cost_items - money_rose_has

    # FA
    answer = money_needed
    return answer