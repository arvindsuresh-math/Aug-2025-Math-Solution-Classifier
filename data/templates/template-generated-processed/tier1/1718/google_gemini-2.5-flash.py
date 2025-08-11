def solve():
    """Index: 1718.
    Returns: how many more fish the fisherman caught than the pelican.
    """
    # L1
    pelican_fish = 13 # A pelican caught 13 fish
    kingfisher_more_than_pelican = 7 # 7 more fish than the pelican
    kingfisher_fish = pelican_fish + kingfisher_more_than_pelican

    # L2
    total_pelican_kingfisher_fish = pelican_fish + kingfisher_fish

    # L3
    fisherman_multiplier = 3 # 3 times the total amount of fish
    fisherman_fish = fisherman_multiplier * total_pelican_kingfisher_fish

    # L4
    fisherman_more_than_pelican = fisherman_fish - pelican_fish

    # FA
    answer = fisherman_more_than_pelican
    return answer