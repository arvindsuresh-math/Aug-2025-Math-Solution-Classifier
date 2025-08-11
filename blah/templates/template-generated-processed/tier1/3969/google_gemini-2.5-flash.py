def solve():
    """Index: 3969.
    Returns: the total recess time students would get that day.
    """
    # L2
    num_As = 10 # 10 As
    extra_minutes_per_A = 2 # 2 extra minutes of recess
    extra_recess_from_As = num_As * extra_minutes_per_A

    # L3
    num_Bs = 12 # 12 Bs
    extra_minutes_per_B = 1 # one extra minute
    extra_recess_from_Bs = num_Bs * extra_minutes_per_B

    # L5
    num_Ds = 5 # 5Ds
    minutes_lost_per_D = 1 # 1 less minute
    minutes_lost_from_Ds = num_Ds * minutes_lost_per_D

    # L6
    initial_recess_minutes = 20 # Students normally get 20 minutes for recess
    total_recess = initial_recess_minutes + extra_recess_from_As + extra_recess_from_Bs - minutes_lost_from_Ds

    # FA
    answer = total_recess
    return answer