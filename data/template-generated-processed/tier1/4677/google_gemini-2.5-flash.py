def solve():
    """Index: 4677.
    Returns: the number of additional rolls of gift wrap Nellie needs to sell.
    """
    # L1
    grandmother_rolls = 1 # 1 roll to her grandmother
    uncle_rolls = 10 # 10 rolls to her uncle
    neighbor_rolls = 6 # 6 rolls to a neighbor
    rolls_sold_initial = grandmother_rolls + uncle_rolls + neighbor_rolls

    # L2
    total_needed_rolls = 45 # sell 45 rolls of gift wrap
    rolls_remaining_to_sell = total_needed_rolls - rolls_sold_initial

    # FA
    answer = rolls_remaining_to_sell
    return answer