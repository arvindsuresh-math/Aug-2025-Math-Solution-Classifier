def solve():
    """Index: 821.
    Returns: the number of pickle slices Ron eats.
    """
    # L1
    sammy_slices = 15 # Sammy can eat 15 pickle slices
    tammy_slices = sammy_slices * 2

    # L2
    ron_fewer_percent_decimal = 0.20 # 20% fewer pickle slices than Tammy
    ron_fewer_percent_num = 20 # 20% fewer pickle slices than Tammy
    percent_factor = 0.01 # WK
    fewer_slices_for_ron = ron_fewer_percent_num * percent_factor * tammy_slices

    # L3
    ron_slices = tammy_slices - fewer_slices_for_ron

    # FA
    answer = ron_slices
    return answer