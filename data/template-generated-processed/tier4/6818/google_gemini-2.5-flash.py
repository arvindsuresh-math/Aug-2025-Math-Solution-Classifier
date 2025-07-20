def solve():
    """Index: 6818.
    Returns: the total cost of chocolate bars.
    """
    # L1
    num_scouts = 15 # 15 scouts
    smores_per_scout = 2 # 2 s'mores each
    total_smores_needed = num_scouts * smores_per_scout

    # L2
    smores_per_bar = 3 # 3 sections to make 3 s'mores
    chocolate_bars_needed = total_smores_needed / smores_per_bar

    # L3
    cost_per_bar = 1.50 # 1 chocolate bar costs $1.50
    total_cost = cost_per_bar * chocolate_bars_needed

    # FA
    answer = total_cost
    return answer