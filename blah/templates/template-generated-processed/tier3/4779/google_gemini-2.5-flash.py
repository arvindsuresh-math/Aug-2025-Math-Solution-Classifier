def solve():
    """Index: 4779.
    Returns: the total profit Melony will make.
    """
    # L1
    profit_per_3_shirts = 21 # Melony makes $21 of profit every time she sells 3 shirts
    sandals_profit_multiplier = 4 # four times as much profit
    profit_for_2_sandals = profit_per_3_shirts * sandals_profit_multiplier

    # L2
    num_sandals_for_profit = 2 # two pairs of sandals
    profit_per_sandal = profit_for_2_sandals / num_sandals_for_profit

    # L3
    num_shirts_for_profit = 3 # sells 3 shirts
    profit_per_shirt = profit_per_3_shirts / num_shirts_for_profit

    # L4
    shirts_to_sell = 7 # sells 7 shirts
    profit_from_shirts = shirts_to_sell * profit_per_shirt

    # L5
    sandals_to_sell = 3 # 3 pairs of sandals
    profit_from_sandals = sandals_to_sell * profit_per_sandal

    # L6
    total_profit = profit_from_shirts + profit_from_sandals

    # FA
    answer = total_profit
    return answer