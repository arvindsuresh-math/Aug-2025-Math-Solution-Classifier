def solve():
    """Index: 5187.
    Returns: the amount of solution in each beaker.
    """
    # L1
    solution_per_test_tube = 7 # 7 mL of solution
    num_test_tubes = 6 # 6 test tubes
    total_solution_ml = solution_per_test_tube * num_test_tubes

    # L2
    num_beakers = 3 # 3 beakers
    solution_per_beaker = total_solution_ml / num_beakers

    # FA
    answer = solution_per_beaker
    return answer