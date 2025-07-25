def solve():
    """Index: 3142.
    Returns: the number of additional liters of oil needed to make the large tanker half-full.
    """
    # L1
    initial_tank_capacity = 4000 # 4000-liter tank
    fraction_numerator = 3 # Three-quarters of the oil
    fraction_denominator = 4 # Three-quarters of the oil
    oil_poured = initial_tank_capacity * (fraction_numerator / fraction_denominator)

    # L2
    initial_oil_in_tanker = 3000 # already had 3000 liters of oil
    current_oil_in_tanker = initial_oil_in_tanker + oil_poured

    # L3
    tanker_capacity = 20000 # 20000-liter capacity tanker
    half_capacity_numerator = 1 # half-full
    half_capacity_denominator = 2 # half-full
    half_tanker_capacity = (half_capacity_numerator / half_capacity_denominator) * tanker_capacity

    # L4
    liters_needed = half_tanker_capacity - current_oil_in_tanker

    # FA
    answer = liters_needed
    return answer