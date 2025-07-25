from fractions import Fraction

def solve():
    """Index: 5946.
    Returns: the total number of gallons of water in both water heaters.
    """
    # L1
    fill_fraction = Fraction(3, 4) # 3/4 full
    wallace_capacity = 40 # capacity of Wallace's water heater is 40 gallons
    wallace_water_gallons = fill_fraction * wallace_capacity

    # L2
    size_ratio = 2 # twice the size
    catherine_capacity = wallace_capacity / size_ratio

    # L3
    catherine_water_gallons = fill_fraction * catherine_capacity

    # L4
    total_gallons = catherine_water_gallons + wallace_water_gallons

    # FA
    answer = total_gallons
    return answer