def solve():
    """Index: 2549.
    Returns: the number of horses that will get new horseshoes at the riding school.
    """
    # L1
    total_iron_kg = 400 # 400kg of iron
    iron_per_horseshoe_kg = 2 # each horseshoe needs 2kg of iron
    total_horseshoes_possible = total_iron_kg / iron_per_horseshoe_kg

    # L2
    num_farms = 2 # 2 farms nearby
    horses_per_farm = 2 # each of which has 2 horses
    horses_for_farms = num_farms * horses_per_farm

    # L3
    num_stables = 2 # 2 stables nearby
    horses_per_stable = 5 # all have 5 horses each
    horses_for_stables = horses_per_stable * num_stables

    # L4
    total_horses_for_orders = horses_for_farms + horses_for_stables

    # L5
    horseshoes_per_horse = 4 # WK
    total_horseshoes_needed_for_orders = total_horses_for_orders * horseshoes_per_horse

    # L6
    horseshoes_left_for_riding_school = total_horseshoes_possible - total_horseshoes_needed_for_orders

    # L7
    horses_for_riding_school = horseshoes_left_for_riding_school / horseshoes_per_horse

    # FA
    answer = horses_for_riding_school
    return answer