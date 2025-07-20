def solve():
    """Index: 3888.
    Returns: the total number of bottles of soda ordered.
    """
    # L1
    cases_april = 20 # 20 cases of bottles of soda in April
    cases_may = 30 # 30 cases in May
    total_cases = cases_april + cases_may

    # L2
    bottles_per_case = 20 # 20 bottles per case
    total_bottles = total_cases * bottles_per_case

    # FA
    answer = total_bottles
    return answer