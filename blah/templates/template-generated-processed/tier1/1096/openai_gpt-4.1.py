def solve():
    """Index: 1096.
    Returns: the number of jellybeans Lorelai has eaten.
    """
    # L1
    rory_more_than_gigi = 30 # Rory has 30 more jellybeans than Gigi
    gigi_jellybeans = 15 # Gigi who has 15 jellybeans
    rory_jellybeans = rory_more_than_gigi + gigi_jellybeans

    # L2
    total_girls_jellybeans = rory_jellybeans + gigi_jellybeans

    # L3
    lorelai_multiplier = 3 # three times the number of jellybeans that both girls have
    lorelai_eaten = lorelai_multiplier * total_girls_jellybeans

    # FA
    answer = lorelai_eaten
    return answer