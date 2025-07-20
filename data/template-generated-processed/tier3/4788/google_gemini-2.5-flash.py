def solve():
    """Index: 4788.
    Returns: the total cost each student will need to spend on uniforms.
    """
    # L1
    pants_cost = 20 # The pants cost $20
    shirt_multiplier = 2 # the shirt costs twice as much as the pants
    shirt_cost = pants_cost * shirt_multiplier

    # L2
    tie_divisor = 5 # the tie costs 1/5 as much as the shirt
    tie_cost = shirt_cost / tie_divisor

    # L3
    socks_cost = 3 # the socks cost $3/pair
    one_uniform_set_cost = pants_cost + shirt_cost + tie_cost + socks_cost

    # L4
    num_uniforms = 5 # Each student needs to buy five complete uniforms
    total_cost_per_student = one_uniform_set_cost * num_uniforms

    # FA
    answer = total_cost_per_student
    return answer