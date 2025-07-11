def solve():
    """Index: 2514.
    Returns: the number of times Boris needs to climb his mountain.
    """
    # L1
    hugo_elevation = 10000 # Hugo's mountain has an elevation of 10,000 feet
    shorter_by = 2500 # 2,500 feet shorter
    boris_elevation = hugo_elevation - shorter_by

    # L2
    hugo_climbs = 3 # Hugo climbed his mountain 3 times
    hugo_total_climb_distance = hugo_climbs * hugo_elevation

    # L3
    boris_climbs_needed = hugo_total_climb_distance / boris_elevation

    # FA
    answer = boris_climbs_needed
    return answer