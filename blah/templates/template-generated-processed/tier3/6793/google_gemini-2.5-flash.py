def solve():
    """Index: 6793.
    Returns: the number of containers of oil each truck will have after redistribution.
    """
    # L1
    trucks_type1_count = 7 # 7 trucks
    boxes_per_truck_type1 = 20 # 20 boxes
    trucks_type2_count = 5 # 5 trucks
    boxes_per_truck_type2 = 12 # 12 boxes
    total_boxes_of_oil = trucks_type1_count * boxes_per_truck_type1 + trucks_type2_count * boxes_per_truck_type2

    # L2
    containers_per_box = 8 # Each box holds 8 containers of oil
    total_containers_of_oil = total_boxes_of_oil * containers_per_box

    # L3
    redistribution_trucks = 10 # redistributed onto 10 trucks
    containers_per_redistributed_truck = total_containers_of_oil / redistribution_trucks

    # FA
    answer = containers_per_redistributed_truck
    return answer