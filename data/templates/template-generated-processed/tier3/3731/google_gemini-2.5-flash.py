def solve():
    """Index: 3731.
    Returns: the total number of coats and uniforms each lab tech gets.
    """
    # L1
    uniforms = 12 # 12 uniforms in the lab
    coats_multiplier = 6 # 6 times as many lab coats
    lab_coats = coats_multiplier * uniforms

    # L2
    total_coats_and_uniforms = lab_coats + uniforms

    # L3
    techs_divisor = 2 # half of the number of uniforms
    lab_techs = uniforms / techs_divisor

    # L4
    coats_and_uniforms_per_tech = total_coats_and_uniforms / lab_techs

    # FA
    answer = coats_and_uniforms_per_tech
    return answer