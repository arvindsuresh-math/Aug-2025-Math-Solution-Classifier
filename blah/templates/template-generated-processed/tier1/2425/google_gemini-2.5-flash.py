def solve():
    """Index: 2425.
    Returns: the number of petals on the remaining daisies in her garden.
    """
    # L1
    daisies_initial = 5 # 5 daisies
    petals_per_daisy = 8 # each daisy has 8 petals
    total_initial_petals = daisies_initial * petals_per_daisy

    # L2
    daisies_given_to_teacher = 2 # gives 2 daisies to her teacher
    petals_given_to_teacher = daisies_given_to_teacher * petals_per_daisy

    # L3
    remaining_petals = total_initial_petals - petals_given_to_teacher

    # FA
    answer = remaining_petals
    return answer