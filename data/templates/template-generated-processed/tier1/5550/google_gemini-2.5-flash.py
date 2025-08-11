def solve():
    """Index: 5550.
    Returns: the total number of lines of the crosswalks in the five intersections.
    """
    # L1
    crosswalks_per_intersection = 4 # 4 crosswalks marked each intersection
    lines_per_crosswalk = 20 # 20 lines per crosswalk
    lines_per_intersection = lines_per_crosswalk * crosswalks_per_intersection

    # L2
    num_intersections = 5 # 5 intersections
    total_lines = lines_per_intersection * num_intersections

    # FA
    answer = total_lines
    return answer