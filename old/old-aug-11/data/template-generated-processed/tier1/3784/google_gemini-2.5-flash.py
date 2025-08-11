def solve():
    """Index: 3784.
    Returns: the total square inches of material Sally will need.
    """
    # L1
    tablecloth_length = 102 # 102 inches
    tablecloth_width = 54 # 54 inches
    tablecloth_area = tablecloth_length * tablecloth_width

    # L2
    num_napkins = 8 # 8 napkins
    napkin_length = 6 # 6 by 7 inches
    napkin_width = 7 # 6 by 7 inches
    napkins_total_area = num_napkins * (napkin_length * napkin_width)

    # L3
    total_material_needed = tablecloth_area + napkins_total_area

    # FA
    answer = total_material_needed
    return answer