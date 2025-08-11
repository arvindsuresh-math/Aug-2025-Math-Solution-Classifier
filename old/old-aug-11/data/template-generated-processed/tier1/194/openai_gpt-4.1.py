def solve():
    """Index: 194.
    Returns: the total cost of the gifts after the rebate.
    """
    # L1
    polo_shirt_price = 26 # $26 each
    num_polo_shirts = 3 # 3 polo shirts
    polo_shirts_total = polo_shirt_price * num_polo_shirts

    # L2
    necklace_price = 83 # $83 each
    num_necklaces = 2 # 2 necklaces
    necklaces_total = necklace_price * num_necklaces

    # L3
    computer_game_price = 90 # 1 computer game for $90
    gifts_total = polo_shirts_total + necklaces_total + computer_game_price

    # L4
    rebate = 12 # $12 rebate
    total_after_rebate = gifts_total - rebate

    # FA
    answer = total_after_rebate
    return answer