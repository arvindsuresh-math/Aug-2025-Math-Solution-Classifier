def solve():
    """Index: 1887.
    Returns: the total of August's answers from solving the three math problems.
    """
    # L1
    first_answer = 600 # answer of 600
    twice = 2 # twice as big
    second_answer = first_answer * twice

    # L2
    sum_first_second = second_answer + first_answer

    # L3
    less_amount = 400 # 400 less than the combined total
    third_answer = sum_first_second - less_amount

    # L4
    total = sum_first_second + third_answer

    # FA
    answer = total
    return answer