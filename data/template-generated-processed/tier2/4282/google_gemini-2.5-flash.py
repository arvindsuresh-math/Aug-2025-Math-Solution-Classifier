def solve():
    """Index: 4282.
    Returns: the total amount Rohan will earn after 6 months.
    """
    # L1
    farm_area = 20 # a 20-square meter coconut farm
    trees_per_sq_meter = 2 # Each square meter has 2 coconut trees
    total_trees = farm_area * trees_per_sq_meter

    # L2
    coconuts_per_tree = 6 # each tree has 6 coconuts
    coconuts_per_harvest = total_trees * coconuts_per_tree

    # L3
    total_months = 6 # after 6 months
    harvest_interval_months = 3 # harvested every 3 months
    num_harvests = total_months / harvest_interval_months
    total_coconuts_6_months = coconuts_per_harvest * num_harvests

    # L4
    cost_per_coconut = 0.50 # each coconut costs $0.50
    total_earnings = total_coconuts_6_months * cost_per_coconut

    # FA
    answer = total_earnings
    return answer