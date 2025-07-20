def solve():
    """Index: 7175.
    Returns: the number of frogs that will need to find a new pond.
    """
    # L1
    initial_frogs = 5 # five frogs living in it
    tadpole_multiplier = 3 # three times as many tadpoles
    initial_tadpoles = tadpole_multiplier * initial_frogs

    # L2
    survival_numerator = 2 # Two-thirds of the tadpoles
    survival_denominator = 3 # Two-thirds of the tadpoles
    surviving_tadpoles = survival_numerator * initial_tadpoles / survival_denominator

    # L3
    total_frogs_after_growth = initial_frogs + surviving_tadpoles

    # L4
    pond_capacity = 8 # The pond can only sustain eight frogs
    frogs_to_relocate = total_frogs_after_growth - pond_capacity

    # FA
    answer = frogs_to_relocate
    return answer