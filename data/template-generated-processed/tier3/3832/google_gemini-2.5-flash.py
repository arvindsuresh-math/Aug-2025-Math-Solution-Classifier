def solve():
    """Index: 3832.
    Returns: the total number of bouquets the florist can make.
    """
    # L1
    seeds_per_color = 125 # 125 seeds for each color of flower
    num_colors = 4 # 4 colors of flower
    total_seeds_planted = seeds_per_color * num_colors

    # L2
    killed_red = 45 # 45 red flowers
    killed_yellow = 61 # 61 yellow
    killed_orange = 30 # 30 orange
    killed_purple = 40 # 40 purple flowers
    total_flowers_killed = killed_red + killed_yellow + killed_orange + killed_purple

    # L3
    remaining_flowers = total_seeds_planted - total_flowers_killed

    # L4
    flowers_per_bouquet = 9 # each bouquet contains 9 flowers
    num_bouquets = remaining_flowers / flowers_per_bouquet

    # FA
    answer = num_bouquets
    return answer