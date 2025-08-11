def solve():
    """Index: 2432.
    Returns: the number of brownies Annie had left.
    """
    # L1
    initial_brownies = 20 # Annie brought 20 brownies to school
    half_divisor = 2 # half of them
    brownies_given_to_faculty = initial_brownies / half_divisor

    # L2
    remaining_brownies_after_faculty = initial_brownies - brownies_given_to_faculty

    # L3
    brownies_given_to_carl = remaining_brownies_after_faculty / half_divisor

    # L4
    remaining_brownies_after_carl = remaining_brownies_after_faculty - brownies_given_to_carl

    # L5
    brownies_given_to_simon = 2 # another two to her friend, Simon
    final_brownies_left = remaining_brownies_after_carl - brownies_given_to_simon

    # FA
    answer = final_brownies_left
    return answer