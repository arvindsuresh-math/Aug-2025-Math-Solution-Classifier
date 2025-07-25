def solve():
    """Index: 2520.
    Returns: the total number of war supplies Rockefeller Army Base has.
    """
    # L1
    grenada_total_supplies = 6000 # 6000 war supplies they have in total
    num_components = 3 # equally divided among the 6000 war supplies they have in total
    grenada_each_component = grenada_total_supplies / num_components

    # L2
    rockefeller_guns_additional = 3000 # 3000 more than twice as many guns
    rockefeller_guns_multiplier = 2 # twice as many guns
    rockefeller_guns = rockefeller_guns_additional + rockefeller_guns_multiplier * grenada_each_component

    # L3
    rockefeller_tractors_multiplier = 3 # thrice as many war tractors
    rockefeller_tractors_deduction = 400 # 400 less than thrice as many war tractors
    rockefeller_tractors = rockefeller_tractors_multiplier * grenada_each_component - rockefeller_tractors_deduction

    # L4
    rockefeller_uniforms_multiplier = 30 # 30 times as many soldier uniforms
    rockefeller_uniforms = rockefeller_uniforms_multiplier * grenada_each_component

    # L5
    total_rockefeller_supplies = rockefeller_uniforms + rockefeller_tractors + rockefeller_guns

    # FA
    answer = total_rockefeller_supplies
    return answer