def solve():
    """Index: 6538.
    Returns: the total number of fence poles placed along the path on both sides.
    """
    # L1
    total_path_length = 900 # a 900-foot path
    bridge_length = 42 # a 42-foot bridge
    path_to_line = total_path_length - bridge_length

    # L2
    pole_spacing = 6 # Every 6 feet, a fence pole is placed
    poles_one_side = path_to_line / pole_spacing

    # L3
    number_of_sides = 2 # on both sides
    total_fence_poles = poles_one_side * number_of_sides

    # FA
    answer = total_fence_poles
    return answer