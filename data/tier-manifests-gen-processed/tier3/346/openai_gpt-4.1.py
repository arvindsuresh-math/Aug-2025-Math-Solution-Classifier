def solve():
    """Index: 346.
    Returns: the number of cans of paint Lucille needs.
    """
    # L1
    wall1_width = 3 # 3 meters wide
    wall1_height = 2 # 2 meters tall
    wall1_area = wall1_width * wall1_height

    # L2
    wall1_count = 2 # Two of her walls
    wall1_total_area = wall1_area * wall1_count

    # L3
    wall3_width = 5 # 5 meters wide
    wall3_height = 2 # 2 meters tall
    wall3_area = wall3_width * wall3_height

    # L4
    wall4_width = 4 # 4 meters wide
    wall4_height = 2 # 2 meters tall
    wall4_area = wall4_width * wall4_height

    # L5
    total_area = wall1_total_area + wall3_area + wall4_area

    # L6
    can_coverage = 2 # each can of paint covers 2 square meters
    cans_needed = total_area / can_coverage

    # FA
    answer = cans_needed
    return answer