from fractions import Fraction

def solve():
    """Index: 3936.
    Returns: the number of women who work in retail in Los Angeles.
    """
    # L1
    total_population = 6000000 # 6 million people living in it
    women_fraction_denominator = 2 # half the population is women
    women_population = total_population / women_fraction_denominator

    # L2
    retail_fraction = Fraction(1, 3) # 1/3 of the women work in retail
    women_in_retail = women_population * retail_fraction

    # FA
    answer = women_in_retail
    return answer