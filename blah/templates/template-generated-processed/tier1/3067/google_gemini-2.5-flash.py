def solve():
    """Index: 3067.
    Returns: the total number of seashells the 3 children had.
    """
    # L1
    aiguo_shells = 20 # Aiguo had 20 seashells
    aiguo_shells_calc = aiguo_shells

    # L2
    vail_less_than_aiguo = 5 # Vail had 5 less than Aiguo
    vail_shells = aiguo_shells - vail_less_than_aiguo

    # L3
    stefan_more_than_vail = 16 # Stefan had 16 more seashells than Vail
    stefan_shells = vail_shells + stefan_more_than_vail

    # L4
    total_shells = aiguo_shells + vail_shells + stefan_shells

    # FA
    answer = total_shells
    return answer