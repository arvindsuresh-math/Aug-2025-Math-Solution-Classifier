def solve():
    """Index: 7367.
    Returns: the total number of baby plants produced by the mother plant.
    """
    # L1
    baby_plants_per_production = 2 # 2 baby plants
    productions_per_year = 2 # 2 times a year
    plants_per_year = baby_plants_per_production * productions_per_year

    # L2
    num_years = 4 # After 4 years
    total_baby_plants = plants_per_year * num_years

    # FA
    answer = total_baby_plants
    return answer