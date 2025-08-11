def solve():
    """Index: 391.
    Returns: the total number of years Tony went to school.
    """
    # L1
    num_degrees_initial = 3 # 1 science degree + 2 more degrees
    years_per_degree = 4 # 4 years to get a degree in science
    years_for_initial_degrees = num_degrees_initial * years_per_degree

    # L2
    years_for_graduate_degree = 2 # another 2 years
    total_years_school = years_for_initial_degrees + years_for_graduate_degree

    # FA
    answer = total_years_school
    return answer