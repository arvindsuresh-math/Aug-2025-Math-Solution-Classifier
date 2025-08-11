from fractions import Fraction

def solve():
    """Index: 1055.
    Returns: the combined population of New York and New England.
    """
    # L1
    ny_fraction = Fraction(2, 3) # two-thirds as populated
    new_england_population = 2100000 # New England has 2100000 people
    new_york_population = ny_fraction * new_england_population

    # L2
    combined_population = new_york_population + new_england_population

    # FA
    answer = combined_population
    return answer