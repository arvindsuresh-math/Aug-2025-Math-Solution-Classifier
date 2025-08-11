def solve():
    """Index: 4265.
    Returns: the total number of coins Zain has.
    """
    # L1
    emerie_quarters = 6 # six quarters
    zain_more_than_emerie = 10 # 10 more of each coin
    zain_quarters = emerie_quarters + zain_more_than_emerie

    # L2
    emerie_dimes = 7 # seven dimes
    zain_dimes = emerie_dimes + zain_more_than_emerie

    # L3
    zain_quarters_dimes_total = zain_dimes + zain_quarters

    # L4
    emerie_nickels = 5 # five nickels
    zain_nickels = zain_more_than_emerie + emerie_nickels

    # L5
    total_zain_coins = zain_quarters_dimes_total + zain_nickels

    # FA
    answer = total_zain_coins
    return answer