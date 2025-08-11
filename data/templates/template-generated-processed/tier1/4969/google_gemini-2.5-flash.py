def solve():
    """Index: 4969.
    Returns: the total cost of the material.
    """
    # L1
    skirt_length = 12 # measures 12 feet
    skirt_width = 4 # by 4 feet
    material_per_skirt = skirt_length * skirt_width

    # L2
    num_overskirt = 1 # an overskirt
    num_petticoats = 2 # two petticoats
    num_skirts = num_overskirt + num_petticoats # an overskirt and two petticoats
    total_material_skirts = material_per_skirt * num_skirts

    # L3
    material_per_sleeve = 5 # 5 square feet of fabric for each of the sleeves
    num_sleeves = 2 # WK
    total_material_sleeves = material_per_sleeve * num_sleeves

    # L4
    material_bodice_shirt = 2 # 2 square feet of material for the shirt
    total_material_all = total_material_sleeves + total_material_skirts + material_bodice_shirt

    # L5
    cost_per_sq_foot = 3 # costs $3 per square foot
    total_cost = total_material_all * cost_per_sq_foot

    # FA
    answer = total_cost
    return answer