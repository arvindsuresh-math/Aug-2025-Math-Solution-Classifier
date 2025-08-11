def solve():
    """Index: 449.
    Returns: the total number of spider legs in the group.
    """
    # L1
    legs_per_spider = 8 # A spider has eight legs
    half_divisor = 2 # half as many legs
    half_legs = legs_per_spider / half_divisor

    # L2
    additional_spiders = 10 # 10 more spiders
    total_spiders = half_legs + additional_spiders

    # L3
    total_legs = legs_per_spider * total_spiders

    # FA
    answer = total_legs
    return answer