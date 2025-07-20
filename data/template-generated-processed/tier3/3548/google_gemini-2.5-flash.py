def solve():
    """Index: 3548.
    Returns: the number of bags of grass seeds Amanda needs.
    """
    # L1
    lot_width = 120 # The lot measures 120 feet
    lot_length = 60 # by 60 feet
    lot_area = lot_width * lot_length

    # L2
    concrete_side = 40 # One section that measures 40 feet by 40 feet
    concrete_area = concrete_side * concrete_side

    # L3
    grassy_area = lot_area - concrete_area

    # L4
    coverage_per_bag = 56 # Each bag of grass seeds covers 56 square feet
    num_bags = grassy_area / coverage_per_bag

    # FA
    answer = num_bags
    return answer