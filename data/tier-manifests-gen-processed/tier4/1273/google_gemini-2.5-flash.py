def solve():
    """Index: 1273.
    Returns: the total amount John paid.
    """
    # L1
    candy_bar_cost = 1.5 # candy bar cost $1.5 each
    gum_cost_divisor = 2 # half as much
    gum_cost_per_pack = candy_bar_cost / gum_cost_divisor

    # L2
    num_gum_packs = 2 # 2 packs of gum
    total_gum_cost = gum_cost_per_pack * num_gum_packs

    # L3
    num_candy_bars = 3 # 3 candy bars
    total_candy_bar_cost = candy_bar_cost * num_candy_bars

    # L4
    total_cost = total_gum_cost + total_candy_bar_cost

    # FA
    answer = total_cost
    return answer