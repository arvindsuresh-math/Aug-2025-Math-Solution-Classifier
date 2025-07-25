def solve():
    """Index: 2616.
    Returns: the number of bottles Don buys from Shop C.
    """
    # L1
    shop_a_bottles = 150 # Shop A normally sells him 150 bottles
    shop_b_bottles = 180 # shop B sells him 180 bottles
    bottles_from_a_and_b = shop_a_bottles + shop_b_bottles

    # L2
    total_capacity = 550 # capable of buying only 550 bottles
    bottles_from_c = total_capacity - bottles_from_a_and_b

    # FA
    answer = bottles_from_c
    return answer