def solve():
    """Index: 6896.
    Returns: the total earnings if all items are sold.
    """
    # L1
    num_candied_apples = 15 # 15 candied apples
    price_per_apple = 2 # $2 each
    earnings_apples = num_candied_apples * price_per_apple

    # L2
    num_candied_grapes = 12 # 12 candied grapes
    price_per_grape = 1.5 # $1.5
    earnings_grapes = num_candied_grapes * price_per_grape

    # L3
    total_earnings = earnings_apples + earnings_grapes

    # FA
    answer = total_earnings
    return answer