def solve():
    """Index: 2447.
    Returns: the total degrees Nathan was warmed up by the blankets.
    """
    # L1
    total_blankets_in_closet = 14 # 14 blankets in his closet
    half_divisor = 2 # half of the 14 blankets
    blankets_added = total_blankets_in_closet / half_divisor

    # L2
    degrees_per_blanket = 3 # Each blanket warms him up by 3 degrees
    total_degrees_warmed = blankets_added * degrees_per_blanket

    # FA
    answer = total_degrees_warmed
    return answer