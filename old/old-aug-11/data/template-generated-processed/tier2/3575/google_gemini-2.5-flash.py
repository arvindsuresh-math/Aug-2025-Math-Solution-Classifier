def solve():
    """Index: 3575.
    Returns: the total number of people in the building.
    """
    # L1
    total_floors = 12 # 12 floors
    half_capacity_decimal = 0.5 # half of them
    full_floors = total_floors * half_capacity_decimal

    # L2
    apartments_per_floor = 10 # each floor has 10 apartments
    apartments_in_full_floors = full_floors * apartments_per_floor

    # L3
    half_full_floors = total_floors - full_floors

    # L4
    apartments_per_half_full_floor = apartments_per_floor * half_capacity_decimal

    # L5
    apartments_in_half_full_floors = half_full_floors * apartments_per_half_full_floor

    # L6
    total_filled_apartments = apartments_in_half_full_floors + apartments_in_full_floors

    # L7
    people_per_apartment = 4 # each apartment has four people
    total_people = total_filled_apartments * people_per_apartment

    # FA
    answer = total_people
    return answer