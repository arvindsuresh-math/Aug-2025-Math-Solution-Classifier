def solve():
    """Index: 5101.
    Returns: the total number of planks of wood Johnny needs.
    """
    # L1
    planks_per_leg = 1 # a plank of wood for each of the legs
    num_legs_per_table = 4 # 4 legs
    planks_for_legs_per_table = planks_per_leg * num_legs_per_table

    # L2
    planks_for_surface_per_table = 5 # 5 planks of wood for the surface
    total_planks_per_table = planks_for_legs_per_table + planks_for_surface_per_table

    # L3
    num_tables = 5 # build 5 tables
    total_planks_needed = total_planks_per_table * num_tables

    # FA
    answer = total_planks_needed
    return answer