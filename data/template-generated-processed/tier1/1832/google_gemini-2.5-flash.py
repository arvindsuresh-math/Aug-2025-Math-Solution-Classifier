def solve():
    """Index: 1832.
    Returns: the number of volleyballs Reynald bought.
    """
    # L1
    soccer_balls = 20 # Twenty were soccer balls
    basketball_more_than_soccer = 5 # five more basketballs than the soccer balls
    num_basketballs = soccer_balls + basketball_more_than_soccer

    # L2
    tennis_multiplier_soccer = 2 # Twice the number of soccer balls
    num_tennis_balls = tennis_multiplier_soccer * soccer_balls

    # L3
    baseball_more_than_soccer = 10 # ten more baseballs than the soccer balls
    num_baseballs = soccer_balls + baseball_more_than_soccer

    # L4
    sum_other_balls = soccer_balls + num_basketballs + num_tennis_balls + num_baseballs
    total_balls = 145 # bought 145 balls
    num_volleyballs = total_balls - sum_other_balls

    # FA
    answer = num_volleyballs
    return answer