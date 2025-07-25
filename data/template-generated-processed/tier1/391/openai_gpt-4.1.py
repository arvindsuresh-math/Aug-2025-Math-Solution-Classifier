def solve():
    """Index: 391.
    Returns: the total number of years Tony went to school to be an astronaut.
    """
    # L1
    num_degrees = 3 # 1 degree in science + 2 more degrees in other fields
    years_per_degree = 4 # each took 4 years
    years_for_degrees = num_degrees * years_per_degree

    # L2
    grad_degree_years = 2 # graduate degree in physics, which took another 2 years
    total_years = years_for_degrees + grad_degree_years

    # FA
    answer = total_years
    return answer