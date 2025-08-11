def solve():
    """Index: 1543.
    Returns: the number of additional sit-ups Bob can do compared to Ken.
    """
    # L1
    ken_situps = 20 # Ken can do 20 sit-ups
    nathan_multiplier = 2 # twice as many
    nathan_situps = ken_situps * nathan_multiplier

    # L2
    combined_ken_nathan_situps = ken_situps + nathan_situps

    # L3
    bob_divisor = 2 # half the number
    bob_situps = combined_ken_nathan_situps / bob_divisor

    # L4
    difference_bob_ken = bob_situps - ken_situps

    # FA
    answer = difference_bob_ken
    return answer