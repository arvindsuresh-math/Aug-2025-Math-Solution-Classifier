def solve():
    """Index: 1333.
    Returns: the number of additional cakes Louise needs to bake.
    """
    # L1
    total_cakes = 60 # She needs 60 cakes in total
    initial_baked_divisor = 2 # has already produced half this many
    initial_baked_cakes = total_cakes / initial_baked_divisor

    # L2
    cakes_left_after_initial_bake = total_cakes - initial_baked_cakes
    today_baked_divisor = 2 # bakes half this amount
    today_baked_cakes = cakes_left_after_initial_bake / today_baked_divisor

    # L3
    cakes_left_after_today_bake = cakes_left_after_initial_bake - today_baked_cakes
    next_day_baked_divisor = 3 # bakes a third of this amount
    next_day_baked_cakes = cakes_left_after_today_bake / next_day_baked_divisor

    # L4
    cakes_needed_to_bake = total_cakes - initial_baked_cakes - today_baked_cakes - next_day_baked_cakes

    # FA
    answer = cakes_needed_to_bake
    return answer