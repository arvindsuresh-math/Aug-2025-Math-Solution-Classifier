def solve():
    """Index: 1956.
    Returns: the total time saved by using a calculator.
    """
    # L1
    time_per_problem_no_calculator = 5 # 5 minutes per problem without a calculator
    time_per_problem_with_calculator = 2 # 2 minutes per problem with a calculator
    time_saved_per_problem = time_per_problem_no_calculator - time_per_problem_with_calculator

    # L2
    num_problems = 20 # 20 problems
    total_time_saved = time_saved_per_problem * num_problems

    # FA
    answer = total_time_saved
    return answer