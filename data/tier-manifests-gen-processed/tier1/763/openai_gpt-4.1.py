def solve():
    """Index: 763.
    Returns: the number of yards of ribbon left after wrapping the gifts.
    """
    # L1
    num_gifts = 6 # 6 gifts
    ribbon_per_gift = 2 # each gift will use 2 yards of ribbon
    total_ribbon_used = num_gifts * ribbon_per_gift

    # L2
    total_ribbon = 18 # Josh has 18 yards of ribbon
    ribbon_left = total_ribbon - total_ribbon_used

    # FA
    answer = ribbon_left
    return answer