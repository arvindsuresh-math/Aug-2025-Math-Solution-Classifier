def solve():
    """Index: 7273.
    Returns: the number of Kia vehicles on the lot.
    """
    # L1
    total_vehicles = 400 # 400 vehicles for sale
    half_divisor = 2 # Half of the vehicles
    dodge_vehicles = total_vehicles / half_divisor

    # L2
    hyundai_divisor = 2 # half as many Hyundai vehicles
    hyundai_vehicles = dodge_vehicles / hyundai_divisor

    # L3
    kia_vehicles = total_vehicles - dodge_vehicles - hyundai_vehicles

    # FA
    answer = kia_vehicles
    return answer