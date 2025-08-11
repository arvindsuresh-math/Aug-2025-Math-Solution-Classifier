def solve():
    """Index: 1912.
    Returns: the total number of boxes Steven can ship in each delivery.
    """
    # L1
    heavier_box_weight = 40 # some of the boxes weigh 40 pounds
    lighter_box_weight = 10 # some of the boxes weigh 10 pounds
    pair_weight = heavier_box_weight + lighter_box_weight

    # L2
    max_truck_load = 2000 # Each truck can carry a load of no more than 2,000 pounds of cargo
    pairs_per_truck = max_truck_load / pair_weight

    # L3
    num_trucks = 3 # Steven has three trucks
    total_pairs_per_delivery = pairs_per_truck * num_trucks

    # L4
    boxes_per_pair = 2 # WK
    total_boxes_per_delivery = total_pairs_per_delivery * boxes_per_pair

    # FA
    answer = total_boxes_per_delivery
    return answer