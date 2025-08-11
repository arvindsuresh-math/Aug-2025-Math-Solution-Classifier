from fractions import Fraction

def solve():
    """Index: 5170.
    Returns: the total liters of the mixture obtained.
    """
    # L1
    total_water_liters = 20 # 20 liters of water
    water_fraction = Fraction(3, 5) # 3/5th of 20 liters of water
    water_amount = total_water_liters * water_fraction

    # L2
    total_vinegar_liters = 18 # 18 liters of vinegar
    vinegar_fraction = Fraction(5, 6) # 5/6th of 18 liters of vinegar
    vinegar_amount = total_vinegar_liters * vinegar_fraction

    # L3
    total_mixture = water_amount + vinegar_amount

    # FA
    answer = total_mixture
    return answer