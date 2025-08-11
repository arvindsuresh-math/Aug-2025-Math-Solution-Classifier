def solve():
    """Index: 4283.
    Returns: the total number of pies they can bake in 7 days.
    """
    # L1
    eddie_pies_per_day = 3 # Eddie can bake 3 pies a day
    num_days = 7 # in 7 days
    eddie_total_pies = eddie_pies_per_day * num_days

    # L2
    sister_pies_per_day = 6 # His sister can bake 6 pies
    sister_total_pies = sister_pies_per_day * num_days

    # L3
    mother_pies_per_day = 8 # his mother can bake 8 pies a day
    mother_total_pies = mother_pies_per_day * num_days

    # L4
    total_pies_all = eddie_total_pies + sister_total_pies + mother_total_pies

    # FA
    answer = total_pies_all
    return answer