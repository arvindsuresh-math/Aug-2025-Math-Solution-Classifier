def solve():
    """Index: 4813.
    Returns: the total cost of the window treatments.
    """
    # L1
    sheers_cost_per_pair = 40.00 # sheers cost $40.00 a pair
    drapes_cost_per_pair = 60.00 # drapes cost $60.00 a pair
    cost_per_window = sheers_cost_per_pair + drapes_cost_per_pair

    # L2
    num_windows = 3 # 3 windows
    total_cost = num_windows * cost_per_window

    # FA
    answer = total_cost
    return answer