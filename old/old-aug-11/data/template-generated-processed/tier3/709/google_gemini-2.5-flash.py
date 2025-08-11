def solve():
    """Index: 709.
    Returns: the total number of meatballs remaining on the plates.
    """
    # L1
    meatballs_per_plate = 3 # 3 meatballs on each spaghetti plate
    num_sons = 3 # Theresa's 3 sons
    total_meatballs_initial = meatballs_per_plate * num_sons

    # L2
    remaining_fraction_denominator = 3 # one-third remaining on the plates
    meatballs_remaining = total_meatballs_initial / remaining_fraction_denominator

    # FA
    answer = meatballs_remaining
    return answer