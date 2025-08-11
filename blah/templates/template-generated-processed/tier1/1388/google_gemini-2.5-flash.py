def solve():
    """Index: 1388.
    Returns: the number of insects remaining in the playground.
    """
    # L1
    spiders = 3 # 3 spiders
    ants = 12 # 12 ants
    ladybugs_found = 8 # 8 ladybugs
    total_insects_found = spiders + ants + ladybugs_found

    # L2
    ladybugs_fly_away = 2 # 2 of them fly away
    insects_remaining = total_insects_found - ladybugs_fly_away

    # FA
    answer = insects_remaining
    return answer