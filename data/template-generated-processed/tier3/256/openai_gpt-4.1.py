from fractions import Fraction

def solve():
    """Index: 256.
    Returns: the actual distance in miles between Pence and Hillcrest.
    """
    # L1
    map_unit_fraction = Fraction(1, 4) # 1/4 inch on the map
    miles_per_map_unit = 8 # represents 8 miles
    inches_per_unit = 1 / map_unit_fraction # how many 1/4 inches in 1 inch
    miles_per_inch = inches_per_unit * miles_per_map_unit

    # L2
    whole_inches = 3 # 3 inches
    miles_for_whole_inches = whole_inches * miles_per_inch

    # L3
    smaller_map_unit_fraction = Fraction(1, 8) # 1/8 inch
    miles_for_smaller_unit = miles_per_map_unit / (map_unit_fraction / smaller_map_unit_fraction)

    # L4
    fractional_inches_numerator = 3 # 3/8 inch
    miles_for_fractional_inches = fractional_inches_numerator * miles_for_smaller_unit

    # L5
    total_miles = miles_for_whole_inches + miles_for_fractional_inches

    # FA
    answer = total_miles
    return answer