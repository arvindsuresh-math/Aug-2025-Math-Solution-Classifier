def solve():
    """Index: 232.
    Returns: the age in years of Jolene and Phil's fourth child.
    """
    # L1
    years_since_first_child = 15 # first child exactly 15 years ago
    first_child_age = years_since_first_child

    # L2
    years_between_first_and_second = 1 # second child exactly one year after the birth of their first child
    second_child_age = first_child_age - years_between_first_and_second

    # L3
    years_between_second_and_third = 4 # third child on the fourth birthday of their second child
    third_child_age = second_child_age - years_between_second_and_third

    # L4
    years_between_third_and_fourth = 2 # Two years after the birth of their third child
    fourth_child_age = third_child_age - years_between_third_and_fourth

    # FA
    answer = fourth_child_age
    return answer