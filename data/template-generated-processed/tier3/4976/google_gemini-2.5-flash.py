from fractions import Fraction

def solve():
    """Index: 4976.
    Returns: the total ounces of water needed to fill all glasses to the brim.
    """
    # L1
    glass_capacity = 6 # 6-ounces of glasses
    fill_fraction = Fraction(4, 5) # 4/5 full of water
    water_per_glass = glass_capacity * fill_fraction

    # L2
    num_glasses = 10 # 10 6-ounces of glasses
    total_water_current = water_per_glass * num_glasses

    # L3
    total_capacity = num_glasses * glass_capacity

    # L4
    water_needed = total_capacity - total_water_current

    # FA
    answer = water_needed
    return answer