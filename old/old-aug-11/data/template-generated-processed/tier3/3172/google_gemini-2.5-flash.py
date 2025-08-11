def solve():
    """Index: 3172.
    Returns: the cost of each bag of chips.
    """
    # L1
    payment_per_friend = 5 # each pay $5
    num_friends = 3 # Three friends
    total_cost_of_chips = payment_per_friend * num_friends

    # L2
    num_bags = 5 # 5 bags of chips
    cost_per_bag = total_cost_of_chips / num_bags

    # FA
    answer = cost_per_bag
    return answer