def solve():
    """Index: 3341.
    Returns: the total number of recorded new coronavirus cases in the state after three weeks.
    """
    # L1
    first_week_cases = 5000 # 5000 new coronavirus cases on a particular week
    fraction_second_week = 1/2 # half as many new coronaviruses cases as the first week
    second_week_cases = fraction_second_week * first_week_cases

    # L2
    third_week_cases = 2000 # 2000 more cases were recorded in the state
    total_cases = second_week_cases + first_week_cases + third_week_cases

    # FA
    answer = total_cases
    return answer