def solve():
    """Index: 3996.
    Returns: twenty less the number of slices of pizza that the waiter ate.
    """
    # L1
    buzz_ratio_part = 5 # ratio of 5:8, with Buzz's ratio being 5
    waiter_ratio_part = 8 # ratio of 5:8
    total_ratio_parts = buzz_ratio_part + waiter_ratio_part

    # L2
    total_slices = 78 # pizza with 78 slices
    waiter_slices = (waiter_ratio_part / total_ratio_parts) * total_slices

    # L3
    twenty_less = 20 # twenty less
    result = waiter_slices - twenty_less

    # FA
    answer = result
    return answer