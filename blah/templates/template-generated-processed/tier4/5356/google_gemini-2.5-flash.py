def solve():
    """Index: 5356.
    Returns: the total yards of fabric Vivi bought.
    """
    # L1
    checkered_fabric_cost = 75.0 # $75 on checkered fabric
    cost_per_yard = 7.50 # $7.50 per yard
    checkered_yards = checkered_fabric_cost / cost_per_yard

    # L2
    plain_fabric_cost = 45.0 # $45 on plain fabric
    plain_yards = plain_fabric_cost / cost_per_yard

    # L3
    total_yards = checkered_yards + plain_yards

    # FA
    answer = total_yards
    return answer