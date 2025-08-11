from fractions import Fraction

def solve():
    """Index: 5748.
    Returns: the total population of the three cities.
    """
    # L1
    lake_view_population = 24000 # If Lake View's population is 24000
    lake_view_more_than_seattle = 4000 # 4000 more people in Lake View than the population in Seattle
    seattle_population = lake_view_population - lake_view_more_than_seattle

    # L2
    seattle_and_lake_view_total = seattle_population + lake_view_population

    # L3
    boise_fraction = Fraction(3, 5) # 3/5 times as many people living in Boise
    boise_population = boise_fraction * seattle_population

    # L4
    total_population_three_cities = seattle_and_lake_view_total + boise_population

    # FA
    answer = total_population_three_cities
    return answer