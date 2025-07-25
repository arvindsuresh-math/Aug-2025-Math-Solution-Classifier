def solve():
    """Index: 1887.
    Returns: the total of August's answers from solving the three math problems.
    """
    # L1
    first_problem_answer = 600 # an answer of 600
    multiplier_twice = 2 # twice as big
    second_problem_answer = first_problem_answer * multiplier_twice

    # L2
    combined_first_second = second_problem_answer + first_problem_answer

    # L3
    less_than_combined = 400 # 400 less
    third_problem_answer = combined_first_second - less_than_combined

    # L4
    total_answers = combined_first_second + third_problem_answer

    # FA
    answer = total_answers
    return answer