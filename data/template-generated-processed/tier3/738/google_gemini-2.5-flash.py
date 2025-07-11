def solve():
    """Index: 738.
    Returns: the remaining length of fence to be whitewashed.
    """
    # L1
    total_fence_length = 100 # 100-foot fence
    ben_whitewashed = 10 # Ben, whitewashed 10 feet
    fence_left_after_ben = total_fence_length - ben_whitewashed

    # L2
    billy_fraction_denominator = 5 # a fifth of the remaining fence
    billy_whitewashed = fence_left_after_ben / billy_fraction_denominator

    # L3
    fence_left_after_billy = fence_left_after_ben - billy_whitewashed

    # L4
    johnny_fraction_denominator = 3 # a third of the fence that was left
    johnny_whitewashed = fence_left_after_billy / johnny_fraction_denominator

    # L5
    remaining_fence = fence_left_after_billy - johnny_whitewashed

    # FA
    answer = remaining_fence
    return answer