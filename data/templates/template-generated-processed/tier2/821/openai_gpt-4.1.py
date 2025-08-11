def solve():
    """Index: 821.
    Returns: the number of pickle slices Ron eats.
    """
    # L1
    sammy_slices = 15 # Sammy can eat 15 pickle slices
    tammy_multiplier = 2 # twice as much as Sammy
    tammy_slices = sammy_slices * tammy_multiplier

    # L2
    percent_fewer_num = 20 # 20% fewer
    percent_fewer_decimal = 0.20 # .20*30
    percent_factor = 0.01 # WK
    fewer_slices = percent_fewer_num * percent_factor * tammy_slices

    # L3
    ron_slices = tammy_slices - fewer_slices

    # FA
    answer = ron_slices
    return answer