from fractions import Fraction

def solve():
    """Index: 3425.
    Returns: the total number of people in Mojave in five years.
    """
    # L1
    increase_factor = 3 # increased three times
    initial_population = 4000 # The population of Mojave was 4000 a decade ago
    current_population = increase_factor * initial_population

    # L2
    predicted_increase_percentage = Fraction(40, 100) # increase by 40%
    predicted_increase_amount = predicted_increase_percentage * current_population

    # L3
    population_in_five_years = current_population + predicted_increase_amount

    # FA
    answer = population_in_five_years
    return answer