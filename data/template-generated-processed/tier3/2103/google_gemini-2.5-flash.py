def solve():
    """Index: 2103.
    Returns: the total pounds of sand needed to fill the box.
    """
    # L1
    sandbox_side_length = 40 # each side being 40 inches long
    sandbox_area = sandbox_side_length * sandbox_side_length

    # L2
    area_per_bag = 80 # 80 square inches of the sandbox
    num_bags_needed = sandbox_area / area_per_bag

    # L3
    weight_per_bag = 30 # a 30-pound bag of sand
    total_sand_weight = num_bags_needed * weight_per_bag

    # FA
    answer = total_sand_weight
    return answer