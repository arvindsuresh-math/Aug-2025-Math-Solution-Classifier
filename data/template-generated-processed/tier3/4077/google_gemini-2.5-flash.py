from fractions import Fraction

def solve():
    """Index: 4077.
    Returns: the population of Lake Bright.
    """
    # L1
    total_population = 80000 # 80000 people
    gordonia_fraction = Fraction(1, 2) # 1/2 times the total population
    gordonia_population = gordonia_fraction * total_population

    # L2
    toadon_percentage = Fraction(60, 100) # 60 percent of Gordonia's population
    toadon_population = toadon_percentage * gordonia_population

    # L3
    gordonia_toadon_total = gordonia_population + toadon_population

    # L4
    lake_bright_population = total_population - gordonia_toadon_total

    # FA
    answer = lake_bright_population
    return answer