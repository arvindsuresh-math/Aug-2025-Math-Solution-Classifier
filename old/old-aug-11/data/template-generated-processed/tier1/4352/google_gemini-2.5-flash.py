def solve():
    """Index: 4352.
    Returns: the total cost of the decorations.
    """
    # L1
    cost_rose = 5 # $5 each
    num_roses_per_centerpiece = 10 # 10 roses
    cost_roses_centerpiece = cost_rose * num_roses_per_centerpiece

    # L2
    cost_lily = 4 # $4 each
    num_lilies_per_centerpiece = 15 # 15 lilies
    cost_lilies_centerpiece = cost_lily * num_lilies_per_centerpiece

    # L3
    num_place_settings_per_table = 4 # 4 place settings
    cost_place_setting = 10 # $10 each to rent
    cost_place_settings_per_table = num_place_settings_per_table * cost_place_setting

    # L4
    cost_linen_tablecloth = 25 # $25 to rent
    total_cost_per_table = cost_roses_centerpiece + cost_lilies_centerpiece + cost_place_settings_per_table + cost_linen_tablecloth

    # L5
    num_tables = 20 # 20 tables
    total_decorations_cost = total_cost_per_table * num_tables

    # FA
    answer = total_decorations_cost
    return answer