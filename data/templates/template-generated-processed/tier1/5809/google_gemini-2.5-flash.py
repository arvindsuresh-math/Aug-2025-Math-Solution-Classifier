def solve():
    """Index: 5809.
    Returns: the weight in kg Daryl needs to leave out of the crates.
    """
    # L1
    num_crates = 15 # 15 crates he can fill
    crate_weight_limit = 20 # 20kg
    total_crate_capacity = num_crates * crate_weight_limit

    # L2
    num_nail_bags = 4 # 4 bags of nails
    weight_per_nail_bag = 5 # each of which weighs 5kg
    total_nail_weight = num_nail_bags * weight_per_nail_bag

    # L3
    num_hammer_bags = 12 # 12 bags of hammers
    weight_per_hammer_bag = 5 # each of which weighs 5 kg
    total_hammer_weight = num_hammer_bags * weight_per_hammer_bag

    # L4
    num_plank_bags = 10 # 10 bags of wooden planks
    weight_per_plank_bag = 30 # each of which weighs 30kg
    total_plank_weight = num_plank_bags * weight_per_plank_bag

    # L5
    total_items_weight = total_nail_weight + total_hammer_weight + total_plank_weight

    # L6
    weight_to_leave_out = total_items_weight - total_crate_capacity

    # FA
    answer = weight_to_leave_out
    return answer