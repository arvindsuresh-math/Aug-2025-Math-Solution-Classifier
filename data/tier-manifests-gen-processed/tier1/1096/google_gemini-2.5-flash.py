def solve():
    """Index: 1096.
    Returns: the number of jellybeans Lorelai has eaten.
    """
    # L1
    rory_more_than_gigi = 30 # 30 more jellybeans
    gigi_jellybeans = 15 # 15 jellybeans
    rory_jellybeans = rory_more_than_gigi + gigi_jellybeans

    # L2
    total_gigi_rory_jellybeans = rory_jellybeans + gigi_jellybeans

    # L3
    lorelai_multiplier = 3 # three times the number
    lorelai_eaten_jellybeans = lorelai_multiplier * total_gigi_rory_jellybeans

    # FA
    answer = lorelai_eaten_jellybeans
    return answer