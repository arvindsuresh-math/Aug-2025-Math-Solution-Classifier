def solve():
    """Index: 654.
    Returns: the total number of pennies Roshesmina has.
    """
    # L1
    initial_pennies_per_compartment = 2 # two pennies in each of the twelve compartments
    added_pennies_per_compartment = 6 # adds 6 more pennies to each compartment
    pennies_per_compartment_after_addition = added_pennies_per_compartment + initial_pennies_per_compartment

    # L2
    num_compartments = 12 # twelve compartments
    total_pennies = num_compartments * pennies_per_compartment_after_addition

    # FA
    answer = total_pennies
    return answer