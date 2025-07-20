def solve():
    """Index: 3547.
    Returns: the total number of gallons James can transport.
    """
    # L1
    base_van_capacity = 8000 # 8000 gallons
    smaller_truck_percent_less = 0.3 # 30% less than that
    smaller_truck_reduction = base_van_capacity * smaller_truck_percent_less

    # L2
    smaller_truck_capacity = base_van_capacity - smaller_truck_reduction

    # L3
    total_vans = 6 # 6 vans
    num_base_capacity_vans = 2 # 2 of them are 8000 gallons
    num_smaller_vans = 1 # 1 of them is 30% less
    num_very_large_trucks = total_vans - num_base_capacity_vans - num_smaller_vans

    # L4
    larger_truck_percent_larger = 0.5 # 50% larger
    larger_truck_increase = base_van_capacity * larger_truck_percent_larger

    # L5
    larger_truck_capacity = base_van_capacity + larger_truck_increase

    # L6
    total_larger_truck_capacity = num_very_large_trucks * larger_truck_capacity

    # L7
    total_base_capacity_vans_capacity = base_van_capacity * num_base_capacity_vans

    # L8
    total_gallons_transported = smaller_truck_capacity + total_base_capacity_vans_capacity + total_larger_truck_capacity

    # FA
    answer = total_gallons_transported
    return answer