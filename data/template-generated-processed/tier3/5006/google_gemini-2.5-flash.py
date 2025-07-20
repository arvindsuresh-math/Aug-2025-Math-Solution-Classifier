def solve():
    """Index: 5006.
    Returns: the cost of each pack of candy.
    """
    # L1
    total_paid = 20 # a $20 bill
    change_received = 11 # gets $11 change
    total_candy_cost = total_paid - change_received

    # L2
    num_packs = 3 # 3 packs of candy
    cost_per_pack = total_candy_cost / num_packs

    # FA
    answer = cost_per_pack
    return answer