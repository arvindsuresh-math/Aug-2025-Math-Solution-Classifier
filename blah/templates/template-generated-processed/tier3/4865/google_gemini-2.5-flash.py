def solve():
    """Index: 4865.
    Returns: the total population after the births.
    """
    # L1
    immigrants = 50000 # 50,000 people immigrate
    emigrants = 30000 # 30,000 people leave
    net_immigration = immigrants - emigrants

    # L2
    initial_population = 300000 # population of 300,000
    population_before_births = initial_population + net_immigration

    # L3
    pregnant_denominator = 8 # 1/8 of the population gets pregnant
    pregnant_people = population_before_births / pregnant_denominator

    # L4
    twins_denominator = 4 # 1/4 of those people have twins
    people_with_twins = pregnant_people / twins_denominator

    # L5
    children_per_twin_birth = 2 # have twins
    children_from_twins = people_with_twins * children_per_twin_birth

    # L6
    children_from_single_births = pregnant_people - people_with_twins

    # L7
    total_population_after_births = population_before_births + children_from_single_births + children_from_twins

    # FA
    answer = total_population_after_births
    return answer