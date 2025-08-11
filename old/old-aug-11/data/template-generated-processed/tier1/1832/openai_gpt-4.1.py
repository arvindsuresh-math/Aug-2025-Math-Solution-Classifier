def solve():
    """Index: 1832.
    Returns: the number of volleyballs Reynald bought.
    """
    # L1
    soccer_balls = 20 # Twenty were soccer balls
    basketballs_more_than_soccer = 5 # five more basketballs than the soccer balls
    basketballs = soccer_balls + basketballs_more_than_soccer

    # L2
    tennis_balls_multiplier = 2 # Twice the number of soccer balls
    tennis_balls = tennis_balls_multiplier * soccer_balls

    # L3
    baseballs_more_than_soccer = 10 # ten more baseballs than the soccer balls
    baseballs = soccer_balls + baseballs_more_than_soccer

    # L4
    total_balls = 145 # Reynald bought 145 balls
    total_non_volleyballs = soccer_balls + basketballs + tennis_balls + baseballs
    volleyballs = total_balls - total_non_volleyballs

    # FA
    answer = volleyballs
    return answer