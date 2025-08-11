def solve():
    """Index: 1165.
    Returns: the total number of shingles Jerry needs to shingle all roofs.
    """
    # L1
    side_length_1 = 20 # 20 feet
    side_length_2 = 40 # 40 feet
    area_one_side = side_length_1 * side_length_2

    # L2
    sides_per_roof = 2 # two slanted rectangular sides
    area_one_roof = area_one_side * sides_per_roof

    # L3
    num_roofs = 3 # 3 roofs
    total_area = area_one_roof * num_roofs

    # L4
    shingles_per_sqft = 8 # 8 shingles to cover one square foot
    total_shingles = total_area * shingles_per_sqft

    # FA
    answer = total_shingles
    return answer