def solve():
    """Index: 1373.
    Returns: the amount of land Jose will have.
    """
    # L1
    jose_share_count = 1 # Jose
    siblings_count = 4 # four siblings
    total_pieces = jose_share_count + siblings_count

    # L2
    total_land = 20000 # 20,000 square meters of land
    jose_land = total_land / total_pieces

    # FA
    answer = jose_land
    return answer