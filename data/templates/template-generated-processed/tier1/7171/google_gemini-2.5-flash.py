def solve():
    """Index: 7171.
    Returns: the total number of crayons produced in 4 hours.
    """
    # L1
    num_colors = 4 # 4 colors of crayons
    crayons_per_color_in_box = 2 # 2 of each color crayon in each box
    crayons_per_box = num_colors * crayons_per_color_in_box

    # L2
    boxes_per_hour = 5 # 5 boxes per hour
    crayons_per_hour = crayons_per_box * boxes_per_hour

    # L3
    production_hours = 4 # in 4 hours
    total_crayons = production_hours * crayons_per_hour

    # FA
    answer = total_crayons
    return answer