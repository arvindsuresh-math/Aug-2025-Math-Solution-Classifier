def solve():
    """Index: 3850.
    Returns: the total number of soda cases needed.
    """
    # L1
    cases_level_1 = 1 # "The top level is just one case."

    # L2
    side_length_level_2 = 2 # derived from question rules
    cases_level_2 = side_length_level_2 * side_length_level_2

    # L3
    side_length_level_3 = 3 # derived from question rules
    cases_level_3 = side_length_level_3 * side_length_level_3

    # L4
    side_length_level_4 = 4 # derived from question rules
    cases_level_4 = side_length_level_4 * side_length_level_4

    # L5
    total_cases = cases_level_1 + cases_level_2 + cases_level_3 + cases_level_4

    # FA
    answer = total_cases
    return answer