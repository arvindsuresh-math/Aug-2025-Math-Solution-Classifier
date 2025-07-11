def solve():
    """Index: 1412.
    Returns: the total number of snails the family of ducks has collectively.
    """
    # L1
    first_group_ducklings = 3 # The first 3 ducklings
    snails_per_duckling_first_group = 5 # find 5 snails each
    snails_first_group = first_group_ducklings * snails_per_duckling_first_group

    # L2
    second_group_ducklings = 3 # Another 3 ducklings
    snails_per_duckling_second_group = 9 # find 9 snails each
    snails_second_group = second_group_ducklings * snails_per_duckling_second_group

    # L3
    total_snails_first_two_groups = snails_first_group + snails_second_group

    # L4
    mother_duck_multiplier = 3 # tree times the total number of snails as the first 2 groups
    mother_duck_snails = total_snails_first_two_groups * mother_duck_multiplier

    # L5
    total_ducklings = 8 # A mother duck as 8 ducklings
    remaining_ducklings = total_ducklings - first_group_ducklings - second_group_ducklings

    # L6
    half_multiplier = 2 # half the number of snails
    snails_per_remaining_duckling = mother_duck_snails / half_multiplier

    # L7
    total_family_snails = total_snails_first_two_groups + mother_duck_snails + snails_per_remaining_duckling + snails_per_remaining_duckling

    # FA
    answer = total_family_snails
    return answer