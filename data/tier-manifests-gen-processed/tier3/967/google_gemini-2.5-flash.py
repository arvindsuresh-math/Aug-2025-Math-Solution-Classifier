from fractions import Fraction

def solve():
    """Index: 967.
    Returns: the temperature decrease of Addison mountain.
    """
    # L1
    decrease_fraction = Fraction(3, 4) # 3/4 of its temperature
    current_temperature = 84 # current temperature of the mountain is 84 degrees
    new_temperature = decrease_fraction * current_temperature

    # L2
    temperature_decrease = current_temperature - new_temperature

    # FA
    answer = temperature_decrease
    return answer