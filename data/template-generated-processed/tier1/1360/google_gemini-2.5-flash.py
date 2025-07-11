def solve():
    """Index: 1360.
    Returns: the number of pumpkins at Sunshine Orchard.
    """
    # L1
    moonglow_pumpkins = 14 # Moonglow Orchard has 14 pumpkins
    multiplier_three_times = 3 # three times the number of pumpkins
    three_times_moonglow = moonglow_pumpkins * multiplier_three_times

    # L2
    more_than_three_times = 12 # 12 more than three times the number
    sunshine_pumpkins = more_than_three_times + three_times_moonglow

    # FA
    answer = sunshine_pumpkins
    return answer