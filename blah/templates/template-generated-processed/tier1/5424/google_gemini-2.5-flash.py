def solve():
    """Index: 5424.
    Returns: the total amount Nancy spends.
    """
    # L1
    num_metal_sets = 2 # two sets of metal beads
    cost_metal_set = 10 # metal beads at $10 each
    cost_metal_beads_total = num_metal_sets * cost_metal_set

    # L2
    cost_crystal_set = 9 # crystal beads at $9 each
    total_spent = cost_crystal_set + cost_metal_beads_total

    # FA
    answer = total_spent
    return answer