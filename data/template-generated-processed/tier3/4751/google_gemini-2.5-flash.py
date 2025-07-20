def solve():
    """Index: 4751.
    Returns: the total number of sandwiches made by Billy, Katelyn, and Chloe.
    """
    # L1
    billy_sandwiches = 49 # Billy made 49 sandwiches
    katelyn_more = 47 # Katelyn made 47 more than that
    katelyn_sandwiches = billy_sandwiches + katelyn_more

    # L2
    chloe_divisor = 4 # a quarter of the amount
    chloe_sandwiches = katelyn_sandwiches / chloe_divisor

    # L3
    total_sandwiches = billy_sandwiches + katelyn_sandwiches + chloe_sandwiches

    # FA
    answer = total_sandwiches
    return answer