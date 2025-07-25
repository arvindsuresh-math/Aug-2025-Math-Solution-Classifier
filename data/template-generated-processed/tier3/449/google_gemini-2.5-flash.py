def solve():
    """Index: 449.
    Returns: the total number of spider legs in the group of spiders.
    """
    # L1
    spider_legs = 8 # A spider has eight legs
    half_divisor = 2 # Half as many legs
    half_spider_legs = spider_legs / half_divisor

    # L2
    more_spiders = 10 # 10 more spiders
    num_spiders_in_group = half_spider_legs + more_spiders

    # L3
    total_legs_in_group = spider_legs * num_spiders_in_group

    # FA
    answer = total_legs_in_group
    return answer