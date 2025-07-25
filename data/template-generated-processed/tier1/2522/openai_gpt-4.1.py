def solve():
    """Index: 2522.
    Returns: the total cost for 1 large and 3 small puzzles.
    """
    # L1
    cost_large = 15 # A large puzzle costs $15
    cost_small_and_large = 23 # A small puzzle and a large puzzle together cost $23
    cost_small = cost_small_and_large - cost_large

    # L2
    num_small = 3 # 3 small puzzles
    cost_three_small = cost_small * num_small

    # L3
    total_cost = cost_three_small + cost_large

    # FA
    answer = total_cost
    return answer