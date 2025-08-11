def solve():
    """Index: 4697.
    Returns: the total number of fish all four people have put together.
    """
    # L1
    billy_fish = 10 # Billy has 10 fish
    tony_multiplier = 3 # 3 times as many fish as Billy's
    tony_fish = tony_multiplier * billy_fish

    # L2
    sarah_more_than_tony = 5 # 5 more fish in her aquarium than Tony does
    sarah_fish = sarah_more_than_tony + tony_fish

    # L3
    bobby_multiplier = 2 # twice as many fish as Sarah's
    bobby_fish = sarah_fish * bobby_multiplier

    # L4
    total_fish = billy_fish + tony_fish + sarah_fish + bobby_fish

    # FA
    answer = total_fish
    return answer