def solve():
    """Index: 654.
    Returns: the total number of pennies Roshesmina has in her piggy bank.
    """
    # L1
    pennies_per_compartment_initial = 2 # two pennies in each of the twelve compartments
    pennies_added_per_compartment = 6 # she adds 6 more pennies to each compartment
    pennies_per_compartment_final = pennies_added_per_compartment + pennies_per_compartment_initial

    # L2
    num_compartments = 12 # twelve compartments
    total_pennies = num_compartments * pennies_per_compartment_final

    # FA
    answer = total_pennies
    return answer