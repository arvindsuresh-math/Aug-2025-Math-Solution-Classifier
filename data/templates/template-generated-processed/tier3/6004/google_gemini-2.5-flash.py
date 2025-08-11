def solve():
    """Index: 6004.
    Returns: the total number of jellybeans needed to fill all glasses.
    """
    # L1
    large_glass_jellybeans = 50 # 50 large jelly beans to fill up a large drinking glass
    half_divisor = 2 # half that amount
    small_glass_jellybeans = large_glass_jellybeans / half_divisor

    # L2
    num_large_glasses = 5 # 5 large drinking glasses
    total_jellybeans_large_glasses = num_large_glasses * large_glass_jellybeans

    # L3
    num_small_glasses = 3 # 3 small ones
    total_jellybeans_small_glasses = num_small_glasses * small_glass_jellybeans

    # L4
    total_jellybeans = total_jellybeans_large_glasses + total_jellybeans_small_glasses

    # FA
    answer = total_jellybeans
    return answer