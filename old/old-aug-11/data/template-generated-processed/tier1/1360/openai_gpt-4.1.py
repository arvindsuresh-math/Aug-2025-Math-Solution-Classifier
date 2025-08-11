def solve():
    """Index: 1360.
    Returns: the number of pumpkins at Sunshine Orchard.
    """
    # L1
    moonglow_pumpkins = 14 # Moonglow Orchard has 14 pumpkins
    multiplier = 3 # three times the number
    three_times_moonglow = moonglow_pumpkins * multiplier

    # L2
    sunshine_extra = 12 # 12 more than three times
    sunshine_pumpkins = sunshine_extra + three_times_moonglow

    # FA
    answer = sunshine_pumpkins
    return answer