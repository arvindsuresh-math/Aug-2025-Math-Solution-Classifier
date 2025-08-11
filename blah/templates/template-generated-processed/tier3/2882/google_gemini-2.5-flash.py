from fractions import Fraction

def solve():
    """Index: 2882.
    Returns: the number of liters of paint left.
    """
    # L1
    gallon_to_liters_conversion = 4 # If a gallon is equal to 4 liters
    dexter_fraction_gallon = Fraction(3, 8) # Dexter used 3/8 of the gallon of paint
    dexter_liters_used = gallon_to_liters_conversion * dexter_fraction_gallon

    # L2
    jay_fraction_gallon = Fraction(5, 8) # Jay used 5/8 of a gallon of paint
    jay_liters_used = gallon_to_liters_conversion * jay_fraction_gallon

    # L3
    total_liters_used_by_dexter_jay = dexter_liters_used + jay_liters_used

    # L4
    num_people_in_scenario = 2 # implied by "they both used" a gallon
    total_initial_liters_assumed = num_people_in_scenario * gallon_to_liters_conversion

    # L5
    liters_left = total_initial_liters_assumed - total_liters_used_by_dexter_jay

    # FA
    answer = liters_left
    return answer