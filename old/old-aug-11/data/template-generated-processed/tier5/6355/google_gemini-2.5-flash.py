def solve():
    """Index: 6355.
    Returns: the number of yards of fabric Louis bought.
    """
    # L2
    num_spools_thread = 2 # two spools of silver thread
    cost_per_spool = 3 # $3 each
    cost_thread = num_spools_thread * cost_per_spool

    # L4
    cost_fabric_per_yard = 24 # $24 per yard
    cost_pattern = 15 # bought a pattern for $15
    total_spent = 141 # spent $141 for the pattern, thread, and fabric
    cost_fabric_total = total_spent - cost_pattern - cost_thread

    # L5
    yards_fabric = cost_fabric_total / cost_fabric_per_yard

    # FA
    answer = yards_fabric
    return answer