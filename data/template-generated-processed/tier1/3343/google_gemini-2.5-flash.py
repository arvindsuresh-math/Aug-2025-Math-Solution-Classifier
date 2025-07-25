def solve():
    """Index: 3343.
    Returns: the total number of jumping jacks Brooke did.
    """
    # L1
    jacks_monday = 20 # 20 jumping jacks on Monday
    jacks_tuesday = 36 # 36 on Tuesday
    jacks_wednesday = 40 # 40 on Wednesday
    jacks_thursday = 50 # 50 on Thursday
    sidney_total_jacks = jacks_monday + jacks_tuesday + jacks_wednesday + jacks_thursday

    # L2
    brooke_multiplier = 3 # three times as many jumping jacks
    brooke_total_jacks = brooke_multiplier * sidney_total_jacks

    # FA
    answer = brooke_total_jacks
    return answer