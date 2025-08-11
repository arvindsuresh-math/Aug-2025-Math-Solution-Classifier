def solve():
    """Index: 5925.
    Returns: the total number of confirmed Coronavirus cases in all states.
    """
    # L1
    new_york_cases = 2000 # 2000 cases of Coronavirus had been confirmed in the state of New York
    half_divisor = 2 # half the number of cases
    california_cases = new_york_cases / half_divisor

    # L2
    more_cases_than_texas = 400 # 400 more cases than the state of Texas
    texas_cases = california_cases - more_cases_than_texas

    # L3
    total_cases = texas_cases + california_cases + new_york_cases

    # FA
    answer = total_cases
    return answer