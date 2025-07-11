def solve():
    """Index: 1388.
    Returns: the number of insects remaining in the playground.
    """
    # L1
    spiders = 3 # Sami finds 3 spiders
    ants = 12 # Hunter sees 12 ants
    ladybugs = 8 # Ming discovers 8 ladybugs
    total_insects = spiders + ants + ladybugs

    # L2
    ladybugs_flew_away = 2 # watches 2 of them fly away
    insects_remaining = total_insects - ladybugs_flew_away

    # FA
    answer = insects_remaining
    return answer