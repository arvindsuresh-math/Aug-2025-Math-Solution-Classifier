from fractions import Fraction

def solve():
    """Index: 2722.
    Returns: the miles per gallon Jim gets.
    """
    # L1
    total_tank_fraction = 1 # WK
    tank_left_fraction = Fraction(2, 3) # 2/3 of a tank left
    tank_used_fraction = total_tank_fraction - tank_left_fraction

    # L2
    total_tank_capacity = 12 # His gas tank is 12 gallons
    gallons_used = total_tank_capacity * tank_used_fraction

    # L3
    trips_count = 2 # to and from work
    distance_one_way = 10 # 10 miles away from his house
    total_miles_driven = trips_count * distance_one_way

    # L4
    miles_per_gallon = total_miles_driven / gallons_used

    # FA
    answer = miles_per_gallon
    return answer