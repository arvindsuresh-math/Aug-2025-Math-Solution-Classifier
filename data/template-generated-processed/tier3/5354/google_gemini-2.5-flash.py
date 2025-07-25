def solve():
    """Index: 5354.
    Returns: the total number of pounds of carrots Kelly harvested.
    """
    # L1
    carrots_bed1 = 55 # In the first bed she pulled out 55 carrots
    carrots_bed2 = 101 # In the second bed she pulled out 101 carrots
    carrots_bed3 = 78 # in the third bed she pulled out 78 carrots
    total_carrots = carrots_bed1 + carrots_bed2 + carrots_bed3

    # L2
    carrots_per_pound = 6 # 6 carrots weighed one pound
    total_pounds = total_carrots / carrots_per_pound

    # FA
    answer = total_pounds
    return answer