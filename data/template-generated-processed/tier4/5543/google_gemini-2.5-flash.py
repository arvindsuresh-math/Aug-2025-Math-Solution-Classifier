def solve():
    """Index: 5543.
    Returns: the total amount John pays.
    """
    # L1
    total_cans = 30 # 30 cans
    buy_one_get_one_free_divisor = 2 # WK
    paid_cans = total_cans / buy_one_get_one_free_divisor

    # L2
    normal_price_per_can = 0.60 # normal price of $0.60
    total_cost = paid_cans * normal_price_per_can

    # FA
    answer = total_cost
    return answer