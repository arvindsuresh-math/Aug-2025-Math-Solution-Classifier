def solve():
    """Index: 7104.
    Returns: the number of additional bags that can be loaded in the truck.
    """
    # L1
    num_boxes = 100 # 100 boxes
    weight_per_box = 100 # 100 kgs each
    total_weight_boxes = num_boxes * weight_per_box

    # L2
    num_crates = 10 # 10 crates
    weight_per_crate = 60 # 60 kgs each
    total_weight_crates = num_crates * weight_per_crate

    # L3
    num_sacks = 50 # 50 sacks
    weight_per_sack = 50 # 50 kilograms each
    total_weight_sacks = num_sacks * weight_per_sack

    # L4
    total_loaded_weight = total_weight_boxes + total_weight_crates + total_weight_sacks

    # L5
    max_capacity = 13500 # maximum of 13,500 kgs of supplies
    remaining_capacity = max_capacity - total_loaded_weight

    # L6
    weight_per_bag = 40 # 40 kilograms each
    num_bags_can_load = remaining_capacity / weight_per_bag

    # FA
    answer = num_bags_can_load
    return answer