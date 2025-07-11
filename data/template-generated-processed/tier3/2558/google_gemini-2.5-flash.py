def solve():
    """Index: 2558.
    Returns: the total number of berets James can make.
    """
    # L1
    red_yarn_spools = 12 # 12 spools of red yarn
    black_yarn_spools = 15 # 15 spools of black yarn
    blue_yarn_spools = 6 # 6 spools of blue yarn
    total_spools = red_yarn_spools + black_yarn_spools + blue_yarn_spools

    # L2
    spools_per_beret = 3 # 3 spools of yarn
    total_berets = total_spools / spools_per_beret

    # FA
    answer = total_berets
    return answer