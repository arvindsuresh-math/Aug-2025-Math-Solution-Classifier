def solve():
    """Index: 4617.
    Returns: the total money Maggie earned.
    """
    # L1
    subscriptions_to_neighbor_one = 2 # 2 to the next-door neighbor
    multiplier_for_other_neighbor = 2 # twice that amount
    subscriptions_to_neighbor_two = subscriptions_to_neighbor_one * multiplier_for_other_neighbor

    # L2
    subscriptions_to_parents = 4 # sells 4 to her parents
    subscriptions_to_grandfather = 1 # 1 to her grandfather
    total_subscriptions = subscriptions_to_parents + subscriptions_to_grandfather + subscriptions_to_neighbor_one + subscriptions_to_neighbor_two

    # L3
    pay_per_subscription = 5.00 # $5.00 for every magazine subscription
    total_earnings = pay_per_subscription * total_subscriptions

    # FA
    answer = total_earnings
    return answer