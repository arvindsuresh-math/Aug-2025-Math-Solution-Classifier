from fractions import Fraction

def solve():
    """Index: 6973.
    Returns: the time in hours to fill the tank to 3/4 of its capacity.
    """
    # L1
    target_fraction = Fraction(3, 4) # 3/4 of its capacity
    tank_capacity = 4000 # capacity of 4000 gallons
    target_volume = target_fraction * tank_capacity

    # L2
    fill_rate = 10 # rate of 10 gallons per hour
    time_to_fill = target_volume / fill_rate

    # FA
    answer = time_to_fill
    return answer