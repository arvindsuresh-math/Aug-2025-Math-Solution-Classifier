def solve():
    """Index: 194.
    Returns: the total cost of the gifts after the rebate.
    """
    # L1
    polo_shirt_price = 26 # 26 each
    num_polo_shirts = 3 # 3 polo shirts
    cost_polo_shirts = polo_shirt_price * num_polo_shirts

    # L2
    necklace_price = 83 # 83 each
    num_necklaces = 2 # 2 necklaces
    cost_necklaces = necklace_price * num_necklaces

    # L3
    computer_game_cost = 90 # 1 computer game for $90
    total_initial_cost = cost_polo_shirts + cost_necklaces + computer_game_cost

    # L4
    rebate_amount = 12 # $12 rebate
    final_cost_after_rebate = total_initial_cost - rebate_amount

    # FA
    answer = final_cost_after_rebate
    return answer