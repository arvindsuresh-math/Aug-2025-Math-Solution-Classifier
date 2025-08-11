from fractions import Fraction

def solve():
    """Index: 4281.
    Returns: the number of minutes it will take Jerry to fill his pond.
    """
    # L1
    normal_pump_rate = 6 # 6 gallons/minute
    restriction_fraction = Fraction(2, 3) # 2/3rds as fast
    current_pump_rate = normal_pump_rate * restriction_fraction

    # L2
    pond_capacity = 200 # The pond can hold 200 gallons of water
    time_to_fill = pond_capacity / current_pump_rate

    # FA
    answer = time_to_fill
    return answer