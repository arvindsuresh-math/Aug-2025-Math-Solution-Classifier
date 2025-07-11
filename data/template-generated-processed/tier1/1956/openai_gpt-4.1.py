def solve():
    """Index: 1956.
    Returns: the total time (in minutes) Matt saves by using a calculator for his homework.
    """
    # L1
    time_per_problem_without = 5 # 5 minutes per problem without a calculator
    time_per_problem_with = 2 # 2 minutes per problem with a calculator
    time_saved_per_problem = time_per_problem_without - time_per_problem_with

    # L2
    num_problems = 20 # assignment has 20 problems
    total_time_saved = time_saved_per_problem * num_problems

    # FA
    answer = total_time_saved
    return answer