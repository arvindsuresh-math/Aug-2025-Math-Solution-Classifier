def solve():
    """Index: 494.
    Returns: the amount the smaller house is being expanded by, in sq. ft.
    """
    # L1
    house_large = 7300 # 7,300 sq. ft. house
    house_small = 5200 # 5,200 sq. ft. house
    original_total = house_large + house_small

    # L2
    new_total = 16000 # new total square footage of both houses is 16,000 sq. ft.
    expansion = new_total - original_total

    # FA
    answer = expansion
    return answer