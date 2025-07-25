def solve():
    """Index: 5066.
    Returns: the average number of people added each year.
    """
    # L1
    year_2005 = 2005 # In 2005
    year_2000 = 2000 # in 2000
    years_passed = year_2005 - year_2000

    # L2
    population_2005 = 467000 # 467 000 people lived in Maryville
    population_2000 = 450000 # 450 000 people lived in Maryville
    total_population_increase = population_2005 - population_2000

    # L3
    average_increase_per_year = total_population_increase / years_passed

    # FA
    answer = average_increase_per_year
    return answer