def solve():
    """Index: 232.
    Returns: the age of their fourth child in years.
    """
    # L1
    first_child_birth_ago = 15 # Their first child exactly 15 years ago
    first_child_age = first_child_birth_ago

    # L2
    second_child_birth_after_first = 1 # exactly one year after the birth of their first child
    second_child_age = first_child_age - second_child_birth_after_first

    # L3
    third_child_birth_after_second = 4 # on the fourth birthday of their second child
    third_child_age = second_child_age - third_child_birth_after_second

    # L4
    fourth_child_birth_after_third = 2 # Two years after the birth of their third child
    fourth_child_age = third_child_age - fourth_child_birth_after_third

    # FA
    answer = fourth_child_age
    return answer