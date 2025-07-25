def solve():
    """Index: 7280.
    Returns: the number of blue stripes on Vaishali's Saree.
    """
    # L1
    multiplier_gold_brown = 3 # three times as many gold stripes as brown stripes
    brown_stripes = 4 # 4 brown stripes
    gold_stripes = multiplier_gold_brown * brown_stripes

    # L2
    multiplier_blue_gold = 5 # five times as many blue stripes as gold stripes
    blue_stripes = multiplier_blue_gold * gold_stripes

    # FA
    answer = blue_stripes
    return answer