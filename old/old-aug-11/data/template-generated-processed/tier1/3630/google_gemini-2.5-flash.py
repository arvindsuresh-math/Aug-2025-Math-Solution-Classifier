def solve():
    """Index: 3630.
    Returns: the total number of doors the company needs to buy.
    """
    # L1
    floors_per_building = 12 # 12 floors each
    num_buildings = 2 # 2 apartment buildings
    total_floors = floors_per_building * num_buildings

    # L2
    apartments_per_floor = 6 # 6 apartments
    total_apartments = apartments_per_floor * total_floors

    # L3
    doors_per_apartment = 7 # 7 doors in total
    total_doors = doors_per_apartment * total_apartments

    # FA
    answer = total_doors
    return answer