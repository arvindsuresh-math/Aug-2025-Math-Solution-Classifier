def solve():
    """Index: 1348.
    Returns: the total cost Simon must spend to make the kabob sticks.
    """
    # L1
    total_cubes_per_slab = 80 # 80 cubes
    cubes_per_kabob = 4 # 4 cubes of beef
    kabob_sticks_per_slab = total_cubes_per_slab / cubes_per_kabob

    # L2
    desired_kabob_sticks = 40 # 40 kabob sticks
    slabs_needed = desired_kabob_sticks / kabob_sticks_per_slab

    # L3
    cost_per_slab = 25 # $25
    total_cost = cost_per_slab * slabs_needed

    # FA
    answer = total_cost
    return answer