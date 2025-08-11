def solve():
    """Index: 4495.
    Returns: the total number of people in the area at the end of 10 years.
    """
    # L1
    initial_population = 100000 # starts at 100,000 people
    birth_increase_percent = 0.6 # increases by 60%
    birth_increase_amount = initial_population * birth_increase_percent

    # L2
    emigration_per_year = 2000 # 2000 people leave per year
    duration_years = 10 # over 10 years
    total_emigration = emigration_per_year * duration_years

    # L3
    immigration_per_year = 2500 # 2500 people come in per year
    total_immigration = immigration_per_year * duration_years

    # L4
    net_migration_increase = total_immigration - total_emigration

    # L5
    final_population = initial_population + birth_increase_amount + net_migration_increase

    # FA
    answer = final_population
    return answer