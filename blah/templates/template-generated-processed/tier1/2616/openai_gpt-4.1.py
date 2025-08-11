def solve():
    """Index: 2616.
    Returns: the number of bottles Don buys from Shop C.
    """
    # L1
    shop_a_bottles = 150 # Shop A normally sells him 150 bottles
    shop_b_bottles = 180 # shop B sells him 180 bottles
    ab_total = shop_a_bottles + shop_b_bottles

    # L2
    total_bottles = 550 # he is capable of buying only 550 bottles
    shop_c_bottles = total_bottles - ab_total

    # FA
    answer = shop_c_bottles
    return answer