def solve():
    """Index: 2240.
    Returns: the price of a pint of frozen yogurt.
    """
    # L1
    num_shrimp_trays = 5 # five trays of jumbo shrimp
    price_per_shrimp_tray = 5 # price of a tray of jumbo shrimp is $5
    cost_shrimp_trays = num_shrimp_trays * price_per_shrimp_tray

    # L2
    total_cost = 55 # for a total of $55
    num_yogurt_pints = 5 # 5 pints of frozen yogurt
    num_gum_packs = 2 # two packs of chewing gum
    cost_yogurt_gum = total_cost - cost_shrimp_trays

    # L3
    gum_cost_divisor = 2 # half as much as a pint of frozen yogurt
    equivalent_yogurt_pints_for_gum = num_gum_packs / gum_cost_divisor

    # L4
    total_equivalent_yogurt_pints = num_yogurt_pints + equivalent_yogurt_pints_for_gum

    # L5
    price_per_yogurt_pint = cost_yogurt_gum / total_equivalent_yogurt_pints

    # FA
    answer = price_per_yogurt_pint
    return answer