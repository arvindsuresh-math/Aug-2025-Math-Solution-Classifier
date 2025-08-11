def solve():
    """Index: 5146.
    Returns: the amount saved per bagel in cents.
    """
    # L1
    bagel_cost_dollars_single = 2.25 # The bagels cost $2.25 each
    cents_per_dollar = 100 # WK
    bagel_cost_cents_single = bagel_cost_dollars_single * cents_per_dollar

    # L2
    dozen_cost_dollars = 24 # a dozen for $24
    dozen = 12 # WK
    bagel_cost_dollars_bulk = dozen_cost_dollars / dozen

    # L3
    bagel_cost_cents_bulk = bagel_cost_dollars_bulk * cents_per_dollar

    # L4
    saved_per_bagel_cents = bagel_cost_cents_single - bagel_cost_cents_bulk

    # FA
    answer = saved_per_bagel_cents
    return answer