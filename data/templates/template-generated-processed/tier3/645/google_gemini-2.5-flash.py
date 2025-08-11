def solve():
    """Index: 645.
    Returns: the maximum number of residents that can live in the block of flats.
    """
    # L1
    total_floors = 12 # This block has 12 floors
    half_divisor = 2 # Half of the floors
    half_floors = total_floors / half_divisor

    # L2
    apartments_per_floor_half1 = 6 # Half of the floors have 6 apartments
    apartments_half1 = half_floors * apartments_per_floor_half1

    # L3
    apartments_per_floor_half2 = 5 # the other half have 5 apartments
    apartments_half2 = half_floors * apartments_per_floor_half2

    # L4
    total_apartments = apartments_half2 + apartments_half1

    # L5
    max_residents_per_apartment = 4 # One apartment can accommodate a maximum of 4 residents
    max_residents = total_apartments * max_residents_per_apartment

    # FA
    answer = max_residents
    return answer