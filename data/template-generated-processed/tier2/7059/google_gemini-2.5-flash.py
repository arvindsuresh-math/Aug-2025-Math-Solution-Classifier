def solve():
    """Index: 7059.
    Returns: the total amount Maddie paid for beauty products.
    """
    # L1
    num_palettes = 3 # 3 different makeup palettes
    cost_per_palette = 15 # cost $15 each
    cost_palettes = num_palettes * cost_per_palette

    # L2
    num_lipsticks = 4 # 4 lipsticks
    cost_per_lipstick = 2.50 # cost $2.50
    cost_lipsticks = num_lipsticks * cost_per_lipstick

    # L3
    num_hair_colors = 3 # 3 boxes of hair color
    cost_per_hair_color = 4 # cost $4 each
    cost_hair_colors = num_hair_colors * cost_per_hair_color

    # L4
    total_cost = cost_palettes + cost_lipsticks + cost_hair_colors

    # FA
    answer = total_cost
    return answer