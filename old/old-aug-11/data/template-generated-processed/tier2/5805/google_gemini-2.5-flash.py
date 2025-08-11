def solve():
    """Index: 5805.
    Returns: the current population of the town.
    """
    # L1
    initial_population = 684 # population of 684 people
    growth_percent_decimal = 0.25 # increased by 25%
    growth_percent_num = 25 # 25% growth spurt
    population_increase = initial_population * growth_percent_decimal

    # L2
    population_after_growth = initial_population + population_increase

    # L3
    moved_away_percent_decimal = 0.40 # 40% of the population moved away
    moved_away_percent_num = 40 # 40% moved away
    population_decrease = population_after_growth * moved_away_percent_decimal

    # L4
    current_population = population_after_growth - population_decrease

    # FA
    answer = current_population
    return answer