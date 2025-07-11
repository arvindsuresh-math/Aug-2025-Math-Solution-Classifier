def solve():
    """Index: 2425.
    Returns: the number of petals on the remaining daisies in Mabel's garden.
    """
    # L1
    total_daisies = 5 # Mabel has 5 daisies
    petals_per_daisy = 8 # each daisy has 8 petals
    total_petals = total_daisies * petals_per_daisy

    # L2
    daisies_given = 2 # she gives 2 daisies to her teacher
    petals_given = daisies_given * petals_per_daisy

    # L3
    petals_remaining = total_petals - petals_given

    # FA
    answer = petals_remaining
    return answer