def solve():
    """Index: 2522.
    Returns: the total cost for 1 large and 3 small puzzles.
    """
    # L1
    total_cost_small_large = 23 # A small puzzle and a large puzzle together cost $23
    cost_large_puzzle = 15 # A large puzzle costs $15
    cost_small_puzzle = total_cost_small_large - cost_large_puzzle

    # L2
    num_small_puzzles_to_buy = 3 # 3 small puzzles
    cost_three_small_puzzles = cost_small_puzzle * num_small_puzzles_to_buy

    # L3
    total_cost = cost_three_small_puzzles + cost_large_puzzle

    # FA
    answer = total_cost
    return answer