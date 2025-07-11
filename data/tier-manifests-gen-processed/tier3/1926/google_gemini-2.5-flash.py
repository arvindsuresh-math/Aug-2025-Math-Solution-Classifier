def solve():
    """Index: 1926.
    Returns: the cost of each pouch in cents.
    """
    # L1
    num_boxes = 10 # 10 boxes of Capri-sun
    pouches_per_box = 6 # Each box has 6 pouches
    total_pouches = num_boxes * pouches_per_box

    # L2
    total_cost_dollars = 12 # he paid $12
    cents_per_dollar = 100 # WK
    total_cost_cents = total_cost_dollars * cents_per_dollar

    # L3
    cost_per_pouch_cents = total_cost_cents / total_pouches

    # FA
    answer = cost_per_pouch_cents
    return answer